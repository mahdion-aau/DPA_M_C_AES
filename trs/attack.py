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
        n_traces = self.trs.number_of_traces
        hw_vec_guess = np.zeros((n_traces, int(self.trs.cryptolen / 2), 256)).astype(int) # Array of hw_vec
        pt = np.zeros((n_traces, int(self.trs.cryptolen / 2)), np.dtype('B'))  # Array of plaintexts
        for i in range(n_traces):
            # Extracting plaintext from TRS file
            [pt_ind, ct_ind] = self.trs.get_trace_data(i)
            pt[i] = pt_ind[0] # Extracting the first byte of plaintext
            # pt[i] = pt_ind # Extracting all 16 bytes of plaintext
            # for j in range(int(self.trs.cryptolen / 2)): # When all 16 bytes are used
            for k_guess in range(256):
                # x = pt[i, 0] # The first byte of plaintext
                sb_out = self.s_box_output(pt[i, 0], k_guess)
                # sb_out = self.s_box_output(pt[i, j], k_guess) # When all 16 bytes are used
                hw_vec_guess[i, 0, k_guess] = self.hw(sb_out)
                # hw_vec_guess[i, j, k_guess] = self.hw(sb_out) # When all 16 bytes are used
        return hw_vec_guess

    def traces(self):
        """ This function extracts all traces from TRS file"""
        n_traces = self.trs.number_of_traces
        all_traces = np.zeros((n_traces, self.trs.number_of_samples), np.int16)  # Array of samples of each trace
        for i in range(n_traces):
            all_traces[i] = self.trs.get_trace_sample(i)
        return all_traces

    def leakage_traces(self):
        """ This function returns transparent traces that is used in corr(hw_vector,leakage_traces)"""
        traces = self.traces()
        trans_traces = traces.transpose()
        return trans_traces

    def attack_dpa(self, hw_ve, leak_traces):
        """ This function computes the correlation between HW and leakage traces and"""
        """ finally, finds the correct key"""
        leak_traces = self.leakage_traces()
        hw_ve = self.hw_model_all_p_key()
        n_samples = self.trs.number_of_samples
        max_corr = 0
        corr = np.zeros(n_samples)
        for i in range(5, n_samples):
            # for j in range(int(self.trs.cryptolen / 2)): # When all 16 bytes are used
            for k_g in range(256):
                c = hw_ve[:, 0, k_g]
                d = leak_traces[i]
                # [corr[i], p_value] = pearsonr(hw_ve[:, j, k_g], leak_traces[i]) # When all 16 bytes are used
                [corr[i], p_value] = pearsonr(hw_ve[:, 0, k_g], leak_traces[i])
                if (abs(corr[i]) > max_corr):
                    max_corr = abs(corr[i])
                    correct_key = k_g
        return [max_corr, hex(correct_key), corr]


if __name__ == "__main__":
    aes_attack = AESAttack()
    aes_attack.read_trs('trs73.trs')
    tr = aes_attack.traces()
    hw_v = aes_attack.hw_model_all_p_key()
    tr_tr = aes_attack.leakage_traces()
    gk = aes_attack.hw_model_all_p_key()
    chw = aes_attack.attack_dpa(hw_v, tr_tr)
    print(aes_attack.attack_dpa(hw_v, tr_tr))
