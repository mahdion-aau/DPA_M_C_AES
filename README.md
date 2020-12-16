DPA_M_C_AES
# DPA attack on Masked_Combined AES

This project is an example of using [GILES](https://github.com/sca-research/GILES) for performing the Differential Power Analyis (DPA) attack on [Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) on **Ubuntu**.


 <!-- toc -->

- [Description](#description)
- [Installing GILES](#installing-GILES)
- [Masked_Combined_AES](#masked-combined-AES)
- [Compiling the target program](#Compiling-the-target-program)
- [Recording leakage traces](#recording-leakage-traces)
- [Analysing recorded traces in python](#analysing-recorded-traces-in-python)
- [First-order DPA attack](#first-order-dpa-attack)
- [Second-order DPA attack](#second-order-dpa-attack)
- [Acknowledgement](#acknowledgement)

<!-- tocstop -->

## Description

In this project the first-order/second-order DPA attacks are carried out on the unmasked/masked and combined version of **AES Encryption** which is implemented in C.
Traces are measured by [GILES](https://github.com/sca-research/GILES) with Hamming weight model as leakage generation model.
All traces are saved in a set file so_called [trs file](https://www.riscure.com/security-tools/inspector-sca/) as output of [GILES](https://github.com/sca-research/GILES).
With the ability of [GILES](https://github.com/sca-research/GILES), in particular `elmo-funcs.h`, the target (S_box) is specified by `start/pause trigger` instructions,and also the random plaintexts are added to traces by `add_to_trace(plaintext,16)` instruction.

The second_order DPA attacks are based on Hamming Weight as prediction function and Pearson's Correlation is used for extracting the key.

The combination functions are the Centered_Product function and Centered_Absolute_Difference[1]. Also they are compared with each other. 

## Installing GILES

## Masked_Combined_AES

## Compiling the target program

## Recording leakage traces

## Analysing recorded traces in python

## First-order DPA attack

## Second-order DPA attack

## Acknowledgement

[1] P.R.B: “Statistical analysis of second order differentialpower analysis,”IEEE Transactions on computers 2009"
