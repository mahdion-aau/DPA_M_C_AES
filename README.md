# DPA_M_C_AES
DPA attack on masked_combined AES

TRS.py module uses trsfile (a library published by Riscure: https://github.com/Riscure/python-trsfile) for extracting traces, data and ... from trs files.

attack.py extracts the first byte of the key. Could be tested with trs39.trs, trs56.trs, trs73.trs and trs90.trs (Name of files: trs+the first byte of the key+.trs).

attack_all_p.py extracts all 16 bytes of the key. Could be tested with si_trs.trs.
