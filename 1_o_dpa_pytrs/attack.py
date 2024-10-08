import pytrs
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

class AESAttack:
    def __init__(self):
        self.sbox = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

    def read_trs(self, filename):
        trace = pytrs.TraceSet(filename)
        # fp = open("trs39.pqc", "wb")
        # trace.Dump(fp)
        # fp = open("trs39.pqc", "rb")
        # trace = pytrs.LoadTraceSet(fp)
        self.pytraces = trace.GetTraces()
        self.data = trace.GetData()
        self.n_t = trace.headers['NT']
        self.n_s = trace.headers['NS']
        self.len_p = trace.headers['DS']

    def get_trace_data(self,ind):  # Gives the data of the index_th trace
        p_ind = np.zeros(int(self.len_p / 2), np.dtype('B'))  # plaintext
        c_ind = np.zeros( int(self.len_p / 2), np.dtype('B'))  # ciphertext
        d_ind = self.data[ind]
        half_cryptolen = int(self.len_p / 2)
        if ind < self.n_t:  # Check the correctness of the number_of_traces
            for i in range(0, self.len_p):
                if i < half_cryptolen:
                    p_ind[i] = d_ind[i]
                else:
                    c_ind[i - half_cryptolen] = d_ind[i]
        return [p_ind, c_ind]

    def s_box_output(self, p, k):
        y = np.zeros(1).astype(int)
        y = self.sbox[p ^ k]
        return y

    def hw(self, x):
        y = np.zeros(1).astype(int)
        y = bin(x).count("1")
        return y

    def hw_model_all_p_key(self):
        """ This function computes HW of the S_BOX output for all bytes of key (256) and n 16_byte plaintexts"""
        """ --> hw_vec_guess(n, 16,256)"""
        hw_vec_guess = np.zeros((self.n_t, int(self.len_p / 2), 256)).astype(int) # Array of hw_vec
        pt = np.zeros((self.n_t, int(self.len_p / 2)), np.dtype('B'))  # Array of plaintexts
        for i in range(self.n_t):
            # Extracting plaintext from TRS file
            [pt_ind, ct_ind] = self.get_trace_data(i)
            pt[i] = pt_ind[0] # Extracting the first byte of plaintext
            for k_guess in range(256):
                sb_out = self.s_box_output(pt[i, 0], k_guess)
                hw_vec_guess[i, 0, k_guess] = self.hw(sb_out)
        return hw_vec_guess

    def traces(self):
        """ This function extracts all traces from TRS file"""
        all_traces = np.zeros((self.n_t, self.n_s), np.int16)  # Array of samples of each trace
        for i in range(self.n_t):
            all_traces[i] = self.pytraces[i].points
        return all_traces

    def leakage_traces(self):
        """ This function returns transparent traces that is used in corr(hw_vector,leakage_traces)"""
        traces = self.traces()
        trans_traces = traces.transpose()
        return trans_traces

    def pearson_corr(self, hw_ve, leak_trc):
        """ When all elements of each input of pearsonr is the same, the output of pearsonr is Nan,
         so there is a warning for solving this warning pearson_check function is defined"""

        def all_same(in_array):
            return all(x == in_array[0] for x in in_array)

        if all_same(hw_ve) ^ all_same(leak_trc):
            corr_pea = 0
        else:
            [corr_pea, p_val] = pearsonr(hw_ve, leak_trc)
        return corr_pea


    def x_axis(self, r1, r2):
        return [item for item in range(r1, r2+1)]

    def plot_trace_input(self, trace):
        """ Plotting the trace as an input"""
        self.trace = trace
        self.x_data = self.x_axis(1, len(trace))
        self.ax.plot(self.x_data, trace)

    def phrase_plot(self, phrase):
        self.ax.plot(self.x_data, self.trace, label=hex(phrase))
        self.ax.legend()

    def plot_show(self, x_l, y_l, title_l, name):
        self.ax.set(xlabel=x_l, ylabel=y_l, title=title_l)
        self.ax.grid()
        self.fig.savefig(name + ".png")
        plt.show()


    def compute_corr(self, hw_vector, leak_traces):
        max_corr = 0
        corr = np.zeros(self.n_s)
        for i in range(self.n_s):
            corr[i] = self.pearson_corr(hw_vector, leak_traces[i])
            if abs(corr[i]) > max_corr:
                max_corr = abs(corr[i])
        return [max_corr, corr]

    def attack_dpa(self, hw_ve, leak_traces):
        max_corr = 0
        max_corr_k = 0
        correct_key = 0
        corr = np.zeros((256, self.n_s))
        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig
        for k_g in range(256):
            [max_corr, corr[k_g]] = self.compute_corr(hw_ve[:, 0, k_g], leak_traces)
            if (max_corr > max_corr_k):
                max_corr_k = max_corr
                correct_key = k_g
            self.plot_trace_input(corr[k_g])
        self.phrase_plot(correct_key)
        self.plot_show('Samples', 'Correlation', 'Corr(HW, traces)', 'corr')
        print('The first byte of the key is:', hex(correct_key))
        print('Dimensions of the Corr matrix: [{0} * {1}]'.format(len(corr), len(corr[0])))
        return [max_corr, hex(correct_key), corr]


if __name__ == "__main__":
    aes_attack = AESAttack()
    aes_attack.read_trs('td5.trs')
    print('The number of traces:', aes_attack.n_t)
    print('The number of plaintexts:', aes_attack.n_t)
    print('The number of samples in a trace:', aes_attack.n_s)
    hw_v = aes_attack.hw_model_all_p_key()
    leakage_traces = aes_attack.leakage_traces()
    attack = aes_attack.attack_dpa(hw_v, leakage_traces)









