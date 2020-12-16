DPA_M_C_AES
# DPA attack on Masked_Combined AES

This project is an example of using [GILES](https://github.com/sca-research/GILES) for performing the Differential Power Analyis (DPA) attack on [Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) on **Ubuntu**.


 <!-- toc -->

- [Description](#description)
- [General Overview of the project](#general-overview-of-the-project)
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

In this project, the **first-order/second-order DPA attacks** are carried out on the **unmasked/masked and combined** version of **AES Encryption**. This version of **AES** called [Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) is implemented in C. 

The related leakage traces used in the DPA attackes are measured by [GILES](https://github.com/sca-research/GILES) which is a software for simulating [side channel analysis](https://en.wikipedia.org/wiki/Side-channel_attack) lekages in **instruction Level**.

The first/second_order DPA attacks are based on **Hamming Weight** as prediction function as well as **Pearson's Correlation** is used for extracting the key.

Furthermore, two combination functions are utilized in the second-order DPA attack, namely **Centered_Product** and **Centered_Absolute_Difference**[1]. The results of these two functions are compared with each other.

## General Overview of the project
To perform a DPA attack on AES, some steps are necessary as following:
1) The 

## Installing GILES
This project is carried out on **Ubuntu operating system**, hence from here **[Download GILES](https://github.com/bristol-sca/GILES/releases)**, the linux version of [GILES](https://github.com/sca-research/GILES) ** GILES-1.1.0-Linux.deb** could be downloaded.


Alternatively, [build it yourself](#building).

## Masked_Combined_AES

## Compiling the target program

## Recording leakage traces
The output of [GILES](https://github.com/sca-research/GILES) is a file with the suffix **.trs**.
with Hamming Weight model as leakage generation model. All traces are automatically stored in a set file so_called [trs file](https://www.riscure.com/security-tools/inspector-sca/) as the output of [GILES](https://github.com/sca-research/GILES). 
With the ability of [GILES](https://github.com/sca-research/GILES), in particular `elmo-funcs.h`, the target  (output of S_box) is specified by `start/pause trigger` instructions,and also the random plaintexts are added to traces by `add_to_trace(plaintext,16)` instruction.


## Analysing recorded traces in python


## First-order DPA attack

## Second-order DPA attack

## Acknowledgement

[1] P.R.B: “Statistical analysis of second order differentialpower analysis,”IEEE Transactions on computers 2009"
