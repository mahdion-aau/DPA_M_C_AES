# DPA_M_C_AES
-----> Uses trsfile module 

"Second_order DPA attack on masked_combined AES"


TRS.py module uses trsfile (a library published by Riscure[1]) for extracting traces, data and ... from trs files.

attack.py extracts the first byte of the key.

attack_all.py extracts all byte of the key and also plots corr_traces separately.


[1]  https://github.com/Riscure/python-trsfile
