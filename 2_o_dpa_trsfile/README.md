# DPA_M_C_AES
-----> Uses trsfile module 

"Second_order DPA attack on masked_combined AES"


TRS.py module uses trsfile (a library published by Riscure[1]) for extracting traces, data and ... from trs files.

attack.py extracts the first byte of the key.Could be tested with 2sh_1a_200.trs (Name of files: Number of shares+the first byte of the key+ Number of traces+.trs).

attack_all.py extracts all byte of the key and also plots corr_traces separately. Could be tested with 2sh_16b_200.trs (Name of files: Number of shares+ 16 byte of the key+ Number of traces+.trs).


[1]  https://github.com/Riscure/python-trsfile
