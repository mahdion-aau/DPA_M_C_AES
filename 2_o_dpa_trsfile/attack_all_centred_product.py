from TRS import TRS
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
        self.trs = TRS(filename)
        self.n_t = self.trs.number_of_traces
        self.n_s = self.trs.number_of_samples
        self.n_s_c_p = int((self.n_s * (self.n_s - 1)) / 2)  # The number of samples in a centered product trace
        self.len_p = self.trs.cryptolen

    def s_box_output(self, p, k):
        y = np.zeros(1).astype(int)
        y = self.sbox[p ^ k]
        return y

    def hw(self, x):
        y = np.zeros(1).astype(int)
        y = bin(x).count("1")
        return y

    def hw_model_all_p_key(self, p_len):
        """ This function computes HW of the S_BOX output for all bytes of key (256) and n 16_byte plaintexts"""
        """ --> hw_vec_guess(n, 1,256)"""
        hw_vec_guess = np.zeros((self.n_t, int(self.len_p / 2), 256)).astype(int) # Array of hw_vec
        pt = np.zeros((self.n_t, int(self.len_p / 2)), np.dtype('B'))  # Array of plaintexts
        for i in range(self.n_t):
            # Extracting plaintext from TRS file
            [pt_ind, ct_ind] = self.trs.get_trace_data(i)
            pt[i] = pt_ind # Extracting the first byte of plaintext
            for k_guess in range(256):
                sb_out = self.s_box_output(pt[i, p_len], k_guess)
                hw_vec_guess[i, p_len, k_guess] = self.hw(sb_out)
        return hw_vec_guess

    def traces(self):
        """ This function extracts all traces from TRS file"""
        all_traces = np.zeros((self.n_t, self.n_s), np.int16)  # Array of samples of each trace
        for i in range(self.n_t):
            all_traces[i] = self.trs.get_trace_sample(i)
        return all_traces

    def mean_sample(self):
        """ This function compute the average of all samples in all traces """
        all_traces = self.traces()
        mean_samp = np.zeros(self.n_s)  # Array of mean of samples
        for i in range(self.n_s):
            mean_samp[i] = np.mean(all_traces[:, i])
        return mean_samp

    def centering_trace(self, trace, mean_sam):
        """ This function centers to zero all samples in a single trace """
        n_samples = len(trace)  # n_samples = self.n_s = self.trs.number_of_samples
        # mean_sam = self.mean_sample()
        centered_trace = np.zeros(n_samples)
        for i in range(n_samples):
            centered_trace[i] = trace[i] - mean_sam[i]
        return centered_trace

    def product_samples(self, trace):
        """ This function calculates (S_i * S_j) i=[0:n_s], j=[i+1:n_s] for a single trace,
            where n is the number of samples and returns a [n_s * (n_s - 1)/2]_vector """
        n = len(trace)  # self.n_s = n_samples = self.trs.number_of_samples
        product_sam = np.zeros(self.n_s_c_p)
        i = 0
        for j in range(n):
            for k in range(j+1, n):
                product_sam[i] = trace[j] * trace[k]
                i += 1
        return product_sam

    def cent_prod_combining_trace(self, trace, mean_sam):
        """ This function returns a trace that is centered and product (n_s * (n_s - 1)/2_vector)"""
        centered_trace = self.centering_trace(trace, mean_sam)
        cent_prod_c_trace = self.product_samples(centered_trace)  # (n_s * (n_s - 1)/2_vector)
        return cent_prod_c_trace

    def comb_traces(self):
        """ This function returns all traces from centred product combining function
            which are used as new traces in dpa attack"""
        traces = self.traces()
        mean_sam = self.mean_sample()
        combined_traces = np.zeros((self.n_t, self.n_s_c_p))  # Array of centered_product_samples of each trace
        for i in range(self.n_t):
            combined_traces[i] = self.cent_prod_combining_trace(traces[i], mean_sam)
        return combined_traces

    def leakage_traces(self):
        """ This function returns transparent traces that is used in corr(hw_vector,leakage_traces)"""
        traces = self.comb_traces()
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

    def compute_corr(self, hw_vector, leak_traces):
        max_corr = 0
        corr = np.zeros(self.n_s_c_p)
        for i in range(self.n_s_c_p):
            corr[i] = self.pearson_corr(hw_vector, leak_traces[i])
            if abs(corr[i]) > max_corr:
                max_corr = abs(corr[i])
        return [max_corr, corr]

    def attack_dpa(self, hw_ve, ax, leak_traces, i_p_len):
        """ This function recovers (the p_len)_th byte of the key"""
        ax.clear()
        max_corr = 0
        max_corr_k = 0
        corr = np.zeros((256, self.n_s_c_p))
        correct_key = 0
        for k_g in range(256):
            [max_corr, corr[k_g]] = self.compute_corr(hw_ve[:, i_p_len, k_g], leak_traces)
            if max_corr > max_corr_k:
                max_corr_k = max_corr
                correct_key = k_g
            ax.plot(corr[k_g])
        ax.set_xlim([1, len(corr[0])])
        # ax.set_ylim([-1, 1])
        ax.title.set_text('Byte {0}=0x{1:2x}'.format(i_p_len, correct_key))
        ax.set_xlabel('Samples')
        ax.set_ylabel('Correlation')
        print('Byte {0} = 0x{1:2x}'.format(i_p_len, correct_key))
        print('Maximum correlation is: {} '.format(max_corr_k))
        print('__________________________________________')
        return [max_corr, hex(correct_key), corr]


if __name__ == "__main__":
    aes_attack = AESAttack()
    aes_attack.read_trs('2sh_16b_60_400.trs')
    p_len = aes_attack.n_s_c_p
    print('The number of traces:', aes_attack.n_t)
    print('The number of samples in a trace:', aes_attack.n_s)
    plt.ion()
    fig = plt.figure()
    i_ax = []
    for i in range(p_len):
        i_ax.append(fig.add_subplot(4, 4, i + 1))

        hw_v = aes_attack.hw_model_all_p_key(i)
        leakage_traces = aes_attack.leakage_traces()
        attack = aes_attack.attack_dpa(hw_v, i_ax[i], leakage_traces, i)

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show()
        plt.tight_layout()
        plt.pause(.001)

    plt.ioff()
    plt.show()
