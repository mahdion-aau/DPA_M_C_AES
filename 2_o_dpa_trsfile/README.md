# DPA_M_C_AES
-----> Uses [trsfile module ](https://trsfile.readthedocs.io/en/latest/)

"Second_order DPA attack on masked_combined AES"


**TRS.py** module uses [trsfile module ](https://trsfile.readthedocs.io/en/latest/) (a library published by [Riscure's Inspector](https://www.riscure.com/security-tools/inspector-sca/)
) for extracting traces, data and ... from trs files.(Written by Nima Mahdion)

**attack_absolute_difference.py** extracts the first byte of the key by making use of centered_absolute_difference combining function.Could be tested with 2sh_5b_400 and 2sh_fc_400.trs (Name of files: Number of shares+the first byte of the key+ Number of traces+.trs).

**attack_centred_product.py** extracts the first byte of the key by making use of centered_product combining function.Could be tested with 2sh_1a_200.trs, 2sh_5b_400 and 2sh_fc_400/300/200.trs (Name of files: Number of shares+the first byte of the key+ Number of traces+.trs).

**attack_all_absolute_difference.py** extracts all byte of the key by making use of centered_absolute_difference combining function. Could be tested with 2sh_16b_200.trs (Name of files: Number of shares+ 16 byte of the key+ Number of traces+.trs).

**attack_all_centered_product.py** extracts all byte of the key by making use of centered_product combining function. Could be tested with 2sh_16b_200.trs (Name of files: Number of shares+ 16 byte of the key+ Number of traces+.trs).

**comparing_diff_and_prod.py** compares 2_O_DPA attacks (just for the first byte of the key) when it is based on centered_absolute_difference and centered_product as combining functions. 2sh_1a_200.trs, 2sh_5b_400 and 2sh_fc_400/300/200.trs (Name of files: Number of shares+the first byte of the key+ Number of traces+.trs).
The results of this comparison is:
1) The value of Pearson (p): p_cent_prod >> p_cent_abs_diff
2) For a successful attack, the number of needed traces (n): n_cent_prod << n_cent_abs_diff


