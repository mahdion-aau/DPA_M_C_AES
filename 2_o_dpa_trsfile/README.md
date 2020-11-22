# DPA_M_C_AES
-----> Uses trsfile module 

"Second_order DPA attack on masked_combined AES"


TRS.py module uses trsfile (a library published by Riscure[1]) for extracting traces, data and ... from trs files.

attack.py extracts the first byte of the key.

attack_all_p.py extracts all 16 bytes of the key. 

attack_all.py extracts all byte of the key by using a function that extracts 1 byte, and also plots corr_traces seperately.


[1]  https://github.com/Riscure/python-trsfile
