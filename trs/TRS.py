# Reading TRS file, Showing Data, Plotting Traces
import trsfile
import numpy as np
import matplotlib.pyplot as plt


class TRS:  # Replacing with trs_reader.py from Si
    def __init__(self, trs_file_name):
        trace_root = trsfile.open(trs_file_name, 'r')
        self.pos = trace_root.engine.data_offset  # data_offset
        headers = trace_root.engine.headers
        for header, value in headers.items():  # Gives the access to key & value f header
            if 'NUMBER_TRACES' in header.name:
                self.number_of_traces = value
            elif 'NUMBER_SAMPLES' in header.name:
                self.number_of_samples = value
            elif 'SAMPLE_CODING' in header.name:
                self.is_float = value.is_float  # sample_coding
            elif 'LENGTH_DATA' in header.name:
                self.cryptolen = value  # length_data is 32 Bytes, the first 16_byte is plaintext and the second 16_byte is ciphertext
        self.traces = [trace_root[i] for i in range(self.number_of_traces)]

    def get_trace_sample(self, ind):  # ind = index # Gives the samples of the index_th trace
        if ind < self.number_of_traces:
            return self.traces[ind].samples

    def get_trace_data(self, ind):  # Gives the data of the index_th trace
        p_ind = np.zeros((1, int(self.cryptolen / 2)), np.dtype('B'))  # plaintext
        c_ind = np.zeros((1, int(self.cryptolen / 2)), np.dtype('B'))  # cipher_text
        d_ind = self.traces[ind].data
        half_cryptolen = int(self.cryptolen/2)
        if ind < self.number_of_traces:  # Check the correctness of the number_of_traces
            for i in range(0, self.cryptolen):
                if i < half_cryptolen:
                    p_ind[0][i] = d_ind[i]
                else:
                    c_ind[0][i-half_cryptolen] = d_ind[i]
        return [p_ind, c_ind]
    
    def x_axis(self,r1, r2):
        return [item for item in range(r1, r2+1)]

    def plot_initial(self):
        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig

    def plot_trace(self, ind=0):
        y_data = trs.get_trace_sample(ind)
        x_data = trs.x_axis(1, len(y_data))
        self.ax.plot(x_data, y_data)

    def plot_show(self):
        self.ax.set(xlabel='Samples', ylabel='Amplitude(HW)', title='GILES')
        self.ax.grid()
        self.fig.savefig("GILES.png")
        plt.show()


if __name__ == "__main__":
    trs = TRS('si_trs.trs')  # Just change the name of the trs file (name.trs)

    trs.plot_initial()
    for i in range(trs.number_of_traces):

        print('-------> The trs file contains {} traces'.format(trs.number_of_traces))
        print('Trace {0:d} contains {1:d} samples'.format(i, trs.number_of_samples))
        print('  - minimum value in trace: {0:f}'.format(min(trs.traces[i])))
        print('  - maximum value in trace: {0:f}'.format(max(trs.traces[i])))
        [plaintext_test, ciphertext_test] = trs.get_trace_data(i)
        print('- Plaintext {}:{}' .format(i,plaintext_test))
        print('- Ciphertext {}:{}'.format(i,ciphertext_test))
        print('_________________________________________________________________________________________')
        trs.plot_trace(i)
    trs.plot_show()



