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


    def trace_input(self):
        traces = self.traces()
        for i in range(self.n_t):
            # Extracting plaintext from TRS file
            [pt_ind, ct_ind] = self.get_trace_data(i)
        return [pt_ind, traces]

    def histog(self):
        [plaintext, trace] = self.trace_input()
        for i in range(self.n_t):
            bins_list = [j for j in range((min(trace[i])), (max(trace[i])))]
            plt.hist(trace[i], bins = bins_list, alpha= 0.7, label = "Input {}".format( i+1))
        plt.ylabel('Frequency')
        plt.xlabel('Power (observed values)')
        plt.title("Leakage Detection");
        plt.legend()
        plt.show()

if __name__ == "__main__":
    leak_det = Leakage_Ditection()
    leak_det.read_trs('2in_16_byte.trs')

    leak_det.histog()

    print('-------> The trs file contains {} traces'.format(leak_det.n_t))
    print('-------> Each trace contains {0:d} samples'.format(leak_det.n_s))

    print('_________________________________________________________________________________________')

    for i in range(leak_det.n_t):
        print('  - minimum value in trace: {0:f}'.format(min(leak_det.traces()[i])))
        print('  - maximum value in trace: {0:f}'.format(max(leak_det.traces()[i])))
        print('- Trace {}:{}'.format(i, leak_det.traces()[i]))


        [plaintext_test, ciphertext_test] = leak_det.get_trace_data(i)
        print('- Plaintext {}:{}'.format(i, plaintext_test))
        print('- Ciphertext {}:{}'.format(i, ciphertext_test))
        print('_________________________________________________________________________________________')









