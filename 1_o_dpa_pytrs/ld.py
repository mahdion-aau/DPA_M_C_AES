import pytrs
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

class Leakage_Ditection:

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

    def traces(self):
        """ This function extracts all traces from TRS file"""
        all_traces = np.zeros((self.n_t, self.n_s), np.int16)  # Array of samples of each trace
        for i in range(self.n_t):
            all_traces[i] = self.pytraces[i].points
        return all_traces


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




    def leakage_detection(self,num_inputs):

        for i in range(num_inputs):
            # Extracting plaintext from TRS file
            [pt_ind, ct_ind] = self.get_trace_data(i)
            for k_guess in range(256):

        return hw_vec_gues
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









