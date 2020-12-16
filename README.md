DPA_M_C_AES
# DPA attack on Masked_Combined AES

This project is an example of using [GILES](https://github.com/sca-research/GILES) for performing the Differential Power Analyis (DPA) attack on Higher-Order-Masked-AES-128[2] (Masked_Combined_AES folder) which is implemented in C language.

Traces are measured by GILES with Hamming weight model as leakage generation model.
All traces are saved in a set file so_called trs [3] as output of GILES.
With the ability of GILES, in particular elmo-funcs.h, the target(S_box) is specified by start/pause trigger instructions,and also the random plaintexts are added to traces by add_to_trace(plaintext,16) instruction.

The second_order DPA attacks are based on Hamming Weight as prediction function and Pearson's Correlation is used for extracting the key.

The combination functions are the Centered_Product function and Centered_Absolute_Difference[4]. Also they are compared with each other. 
 

[1] https://github.com/sca-research/GILES

[2] https://github.com/knarfrank/Higher-Order-Masked-AES-128

[3] https://www.riscure.com/security-tools/inspector-sca/

[4] P.R.B: “Statistical analysis of second order differentialpower analysis,”IEEE Transactions on computers 2009"
