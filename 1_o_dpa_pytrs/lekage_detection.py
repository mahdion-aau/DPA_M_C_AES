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
        color_mean_line=["orange", "blue"]
        for i in range(self.n_t):
            mean_t = np.mean(trace[i])
            var_t = np.var(trace[i])
            std_t = np.std(trace[i])
            print('mean {0:d} : {1:f}'.format(i,mean_t))
            print('var {0:d} : {1:f}'.format(i, var_t))
            print('std {0:d} : {1:f}'.format(i, std_t))
            stats_txt = '\n'.join(['n:', 'Mean:', 'SD:'])
            stats = '\n'.join((
                '{}'.format(len(trace[i])),
                '{:0.2f}'.format(np.mean(trace[i])),
                '{:0.2f}'.format(np.std(trace[i]))))
            bins_list = [j for j in range(min(trace[i])-1 , max(trace[i])+2)]
            plt.hist(trace[i], bins = bins_list, alpha= 0.7, label = "Input {}".format( i+1))
            plt.axvline(trace[i].mean(), color=color_mean_line[i], linestyle='dashed', linewidth=1)
        text_1 = "$\mu_1=%.2f$ {:f}".format(trace[0].mean()) + "\n$\sigma^2_1=%.2f$ {:f}".format(trace[0].var()) + "\n$\sigma_1=%.2f$ {:f}".format(trace[0].std())
        text_2=  "$\mu_2=%.2f$ {:f}".format( trace[1].mean()) +"\n$\sigma^2_2=%.2f$ {:f}".format( trace[1].var()) +"\n$\sigma_2=%.2f$ {:f}".format(trace[1].std())

        plt.text(20, 2500, text_1, size=10,
                 va="baseline", ha="left", multialignment="left",
                 bbox=dict(fc="none"))
        plt.text(20, 1700, text_2, size=10,
                 va="baseline", ha="left", multialignment="left",
                 bbox=dict(fc="none"))

        plt.ylabel('Frequency')
        plt.xlabel('Power (observed values)')
        plt.title("Leakage Detection");
        plt.legend()
        plt.show()

if __name__ == "__main__":
    leak_det = Leakage_Ditection()
    leak_det.read_trs('2in_2sh_9f.trs')

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









