# DPA_M_C_AES
-----> Uses [trsfile module[(https://github.com/Riscure/python-trsfile)

"First_order DPA attack on unmasked_combined AES"

**TRS.py** module uses [trsfile module[(https://github.com/Riscure/python-trsfile) (a library published by [Riscure's Inspector](https://www.riscure.com/security-tools/inspector-sca/)
) for extracting traces, data and ... from trs files.(Written by Nima Mahdion)

**attack.py** extracts the first byte of the key. Could be tested with trs39.trs, trs56.trs, trs73.trs and trs90.trs (Name of files: trs+the first byte of the key+.trs).

**attack_all.py** extracts all byte of the key and also plots corr_traces separately.Could be tested with si_trs.trs.
