# DPA_M_C_AES
-----> Uses pytrs module  [1]

"First_order DPA attack on unmasked_combined AES"

pytrs.py module is used for extracting traces, data and ... from trs files (Written by Yan Yan)

attack.py extracts the first byte of the key. Could be tested with trs39.trs, trs56.trs, trs73.trs and trs90.trs (Name of files: trs+the first byte of the key+.trs).

attack_all.py extracts all byte of the key and also plots corr_traces separately.Could be tested with si_trs.trs.

[1]  https://github.com/sca-research/PyMod4Trs
