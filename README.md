# DPA_M_C_AES
DPA attack on masked_combined AES

This project is related to performing the Differential Power Analyis (DPA) attack on Higher-Order-Masked-AES-128[1] which is implemented in C language.

Traces are measured by GILES[2] with Hamming weight model as leakage generation model.
All traces are saved in a set file so_called TRS[3] as output of GILES.
With the ability of GILES, in particular elmo-funcs.h, the target(S_box) is specified by start/pause trigger, random plaintexts are added to traces.

The attack is based Hamming Weight as prediction function and Pearson's Correlation is used for extracting the key.

The combination function is the Centered_Product function[4]. 
 



[1] https://github.com/knarfrank/Higher-Order-Masked-AES-128

[2] https://github.com/sca-research/GILES

[3] https://www.riscure.com/security-tools/inspector-sca/

[4] P.R.B: “Statistical analysis of second order differentialpower analysis,”IEEE Transactions on computers 2009"
