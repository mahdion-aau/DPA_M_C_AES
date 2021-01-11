DPA_M_C_AES
# DPA attack on Masked_Combined AES
This project is an example of using
[GILES](https://github.com/sca-research/GILES) for performing 
the Differential Power Analysis (DPA) attacks on a **32-bit ARM 
Cortex-M0** microprocessor. The targeted encryption algorithm is
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
which is implemented in _C_ language programming. Furthermore, 
the DPA attacks are written in **Python script** as well as
all steps in the 
current project are run on **Ubuntu**.


 <!-- toc -->

- [General overview of the project](#general-overview-of-the-project)
- [GILES](#giles)
  * [Installing GILES](#installing-giles)
  * [Input of GILES](#input-of-GILES)
  * [Applicable features of GILES](#applicable-features-of-giles)
   
- [Modified_Higher-Order-Masked-AES-128](#modified_higher-order-masked-aes-128)
- [Masked_Combined AES for ARM Cortex-M0](#masked_combined-aes-for-arm-cortex-m0)
- [Compiling the targeted program](#compiling-the-targeted-program)
- [Recording leakage traces](#recording-leakage-traces)
- [Analysing recorded traces and data in a trs file](#analysing-recorded-traces-and-data-in-a-trs-file)
  * [Construction of a trs file](#Construction-of-a-trs-file)
  * [Reading the content of a trs file](#reading-the-content-of-a-trs-file)
- [DPA attacks](#dpa-attacks)
    * [First-order DPA attack](#first-order-dpa-attack)
    * [Second-order DPA attack](#second-order-dpa-attack)
 - [References](#references)

<!-- tocstop -->

## General overview of the project
Here, the **first/second-order DPA attacks**
are carried out on the **unmasked/masked** and **combined**
version of **AES Encryption**. This version of **AES** called 
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128)
is implemented in _C_. The attacks target the output of 
S-Box in the first round. 

The leakage traces (used in the DPA attacks) are measured
by [GILES](https://github.com/sca-research/GILES) 
with  [Hamming Weight](https://en.wikipedia.org/wiki/Hamming_Weight)
leakage model. This means samples of leakage traces indicate
the [Hamming Weight](https://en.wikipedia.org/wiki/Hamming_Weight)
of operands in each related instruction.

The first/second-order DPA attacks are based on **Hamming Weight 
model** as prediction function and **Pearson's Correlation**
is used for distinguishing the correct key.

In addition, two **combination functions** are utilized in the 
second-order DPA attacks, namely, **Centered_Product** and
**Centered_Absolute_Difference**[1] and the results of these two
functions are compared with each other.

To perform a DPA attack on 
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
by using [GILES](https://github.com/sca-research/GILES), 
some steps are necessary as following:
1) Specifying the targeted implementation of AES that can be 
   compiled by "**arm-none-eabi**" compiler. In this project, 
   the targeted _C_ code is "_**Masked_Combined_AES**_" that is the modified 
   version of
   [Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
   and also the exact target is the output of S_Box in the first 
   round. 
2) Compiling the target code by 
   [Thumb Timing Simulator](https://github.com/bristol-sca/thumb-sim)
   to generate a "_**.bin**_" file as the input of
   [GILES](https://github.com/sca-research/GILES).
3) Recording 
   [side channel](https://en.wikipedia.org/wiki/Side-channel_attack) 
   leakage traces  and desirable data in a
   ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
   file by using
   [GILES](https://github.com/sca-research/GILES).
4) Analyzing stored information in the
   ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
   file, which are
   **leakage traces** and **Random Plaintexts** and so on 
   in _Python_ codes.  
5) Performing attacks in _Python_ codes.
## GILES
[GILES](https://github.com/sca-research/GILES) is a
software that 
simulates, emulates and records
**leakages** in **Instruction Level** for an implementation
(e.g. AES encryption written in _**C**_) of a 
hardware device (e.g. ARM Cortex-M0). As a result,
[GILES](https://github.com/sca-research/GILES)
is a tool for detecting and fixing
[side channel analysis](https://en.wikipedia.org/wiki/Side-channel_attack)
and [fault injection](https://en.wikipedia.org/wiki/Fault_injection)
vulnerabilities.  

### Installing GILES
This project is carried out on **Ubuntu operating system**, 
hence firstly, from [here](https://github.com/bristol-sca/GILES/releases)
the linux version of [GILES](https://github.com/sca-research/GILES), 
"_**GILES-1.1.0-Linux.deb**_" should be downloaded. 
Then, to install
[GILES](https://github.com/sca-research/GILES), open a terminal 
(`Ctrl+Alt+T`) and go to the **Downloads** folder:

`$ cd Downloads`

Next, run one of the following commands to install
[GILES](https://github.com/sca-research/GILES):

`$ sodu apt-get install ./GILES-1.1.0-Linux.deb`

or

`$ sudo dpkg -i GILES-1.1.0-Linux.deb`

With the below mentioned commands, all related flags to
[GILES](https://github.com/sca-research/GILES)
are printed:

`$ GILES --help` or `$ GILES -h`


### Input of GILES
The input of [GILES](https://github.com/sca-research/GILES) is a
"_**.bin**_" file. It means there is a need to compile the targeted
program with a **Simulator** to generate the corresponding input 
of [GILES](https://github.com/sca-research/GILES).
For the current project,
[Thumb Timing Simulator](https://github.com/bristol-sca/thumb-sim) 
is considered as the **Simulator** which is the only Simulator 
supported by [GILES](https://github.com/sca-research/GILES)
at this time.

### Applicable features of GILES
[GILES](https://github.com/sca-research/GILES) provides different
features such as:

1) Two leakage models 
([ELMO Power Model](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/mccann)
and [Hamming Weight](https://en.wikipedia.org/wiki/Hamming_Weight)) 
   for simulating leakage traces 

2) Performing [side channel attacks](https://en.wikipedia.org/wiki/Side-channel_attack)
and 
   [Fault Injection attacks](https://en.wikipedia.org/wiki/Fault_injection)

3) Storing all information in a ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
 file that is a standard format designed by 
   [Riscure's Inspector](https://www.riscure.com/security-tools/inspector-sca/)

Besides, all specifications mentioned above, one of pleasant
features of [GILES](https://github.com/sca-research/GILES)
is 
[_**elmo-funcs.h**_](https://github.com/sca-research/GILES/releases) 
library. This provides interesting functions such
as `start/pause_trigger()` that gives the opportunity
to select the target instruction/instructions and also
`add_to_trace()` function for storing the favorable data and 
other functions.




## Modified_Higher-Order-Masked-AES-128

The implementation of 
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
in _C_ language programming is the target in this example, however
it will be modified later. This kind of implementation provides 
more efficiency by making use of the **Common Shares** [2] and the
**Random Reduction** [3] methods.
The implementation can be used for different number of masks/shares,
which is the reason behind the name of 
**Higher-Order-Masked-AES-128**. The order of
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
can be changed by modifying the value of the constant variable
`NUM_SHARES` in the "_**masked_combined.h**_" file.

Regarding the goal of this example, some instructions in 
the implementation of 
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128)
are modified as following:


1) Adding odd number masks/shares
   
   The existed Higher-Order-Masked-AES-128 implementation in
   [this github page](https://github.com/knarfrank/Higher-Order-Masked-AES-128) 
   is compatible with **even number masks/shares** 
   (2, 4, 6 and ... shares). In order to make this also adaptable for
   **odd number masks/shares** (share 1 which is considered as unmasked
   one, 3 , 5, ... shares), some instructions must be added to the
   "_**masked_combined.c**_" file as following:
   + Between lines 217 and 218:
      ```
      if ((NUM_SHARES & 1)==1){
       w[j][NUM_SHARES-1]=h[z[j][NUM_SHARES-1]];
     }
      ```   

   + Between lines 307 and 308:
      ```
      if ((NUM_SHARES & 1)==1){ 
          a0[NUM_SHARES-1]=aa0[NUM_SHARES-1];
          a1[NUM_SHARES-1]=aa1[NUM_SHARES-1]; 
          y0[NUM_SHARES-1]=h[aa0[NUM_SHARES-1]];
          y1[NUM_SHARES-1]=h[aa1[NUM_SHARES-1]];
       } 
       ```
2) Random number generator
   
   It is obvious that all shares/masks should be produced randomly by a robust
      **random number generator (RNG)**. Hence, in 
   the "_**maths.c**_" file 
      (lines 54 to 57), the `getRand()` function is removed and
   instead of that a **RNG** based **LFSR** 
      (written by Frank) is replaced by adding the "_**rand.c**_",
   and the "_**rand.h**_" file.


3) Makefile
   
   To test the result of the program (regarding adding
   **RNG_based_LFSR**) the Makefile should be edited as follows:
   ```
   all
        gcc main.c masked_combined.c maths.c rand.c
   ```
**Note**: Modified_Higher-Order-Masked-AES-128
is a _C_ program that can be run on **Ubuntu operating system**, 
thus it can be compiled by a 
[**Native compiler**](https://en.wikipedia.org/wiki/Compiler). 
A popular _C_/_C++_ compiler
under **Linux/Ubuntu operating system** is
[**GCC**](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
compiler. [Here](https://itsfoss.com/run-c-program-linux/)
is an example related to the GCC compiler under Linux.
 
The **Modified_Higher-Order-Masked-AES-128** program in this project 
is the modified version of
[Higher-Order-Masked-AES-128](https://github.com/knarfrank/Higher-Order-Masked-AES-128)
that can be downloaded.

Now, for compiling and running the program, open a terminal and run
 these command:

 `$ cd Higher-Order-Masked-AES-128`

 `$ make` This command generates the executable file in 
 the format "_**a.out**_".
 
`$ ./a.out` This command runs the executable 
file "_**a.out**_", and prints the Ciphertext 
 in the terminal.

## Masked_Combined AES for ARM Cortex-M0
Here, the purpose is performing **DPA attacks**. 
As a result, this is necessary to generate 
**Random Plaintexts** and also determine the target
which is the output of S_Box in the first round of
**Higher-Order-Masked-AES-128** program. For achieving this goal, 
some modifications are carried out on
**Higher-Order-Masked-AES-128** program existed in this project.
1) Adding ["_**elmo-funcs.h**_"](https://github.com/sca-research/GILES/releases)
   library to "_**masked_combined.c**_" file:
    
    + Making use of `start/pause trigger` instructions
   to specify the target in "_**masked_combined.c**_" file.
   + Initializing the **LFSR** in "_**rand.c**_" 
   by `get_rand()` function. 
   + Utilizing `add_to_trace()`
   function to store **Random Plaintexts** and related
     **Ciphertexts** in 
     ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/).  
   
2) Removing `printf` instructions (This instruction can
   not be compiled by "arm-none-eabi" compiler.)

The modified version is in the "_**Masked_Combined_AES**_" 
folder.

**Note:** According to the section
 [Modified_Higher-Order-Masked-AES-128](#Modified_higher-order-masked-aes-128), 
this program should be compiled by a
[**Native compiler**](https://en.wikipedia.org/wiki/Compiler) 
like  **_C_ / _C++_ compiler GCC**. Here, the goal is 
 generating
 an executable program which can be run on a **32-bit ARM Cortex-M0**
 processor. For compiling the "_**Masked_Combined_AES**_" program for
 this kind of processor on **Ubuntu operating system**, 
 a [**Cross compiler**](https://en.wikipedia.org/wiki/Cross_compiler)
 should be used. There are several **GNU GCC Cross-Compiler** for
 **ARM** microprocessors such as **arm-none-linux-gnueabi**,
 **arm-none-eabi**, **arm-eabi** and so on which are 
 different in some aspects. The suitable one for the current 
 project is "**arm-none-eabi**" toolchain and can be installed
 on **Ubuntu** by the below command:

`$ sudo apt-get install -y gcc-arm-none-eabi`

For checking the installed version use this command: 

    `arm-none-eabi-gcc --version`

## Compiling the targeted program

As mentioned earlier, for compiling the targeted program
("_**Masked_Combined_AES**_") 
and generating the "_**.bin**_"
file as the input of [GILES](https://github.com/sca-research/GILES),
[Thumb Timing Simulator](https://github.com/bristol-sca/thumb-sim)
is used here. 
For compiling, some steps should be done as follows:

1) Downloading
   [Thumb Timing Simulator](https://github.com/bristol-sca/thumb-sim):
   
    `$ cd git clone https://github.com/sca-research/thumb-sim`
2) Copy/paste all the files in the "_**Masked_Combined_AES**_" 
   folder to "_**thumb-sim/example**_" folder.
   
3) Editing the 27-th line of the existed "_**Makefile**_" in
   the "_**thumb-sim/example**_" folder as below:
   `CSRCS     = main.c masked_combined.c maths.c rand.c`
   
4) Now, for compiling the targeted program, [there](https://github.com/bristol-sca/thumb-sim)
   is a guidance, or the below commands can be used:

    ```
     $  cd thumb-sim/
     $  mkdir build 
     $  cd build
     $  cmake ..
     $  make
     $  cmake --build .
     $  cd ..
     $  make -C example
     $  cd example/
    ```
Now the "_**.bin**_" file is generated in the "_**example**_" folder.
Here, the "_**.bin**_" file is named as "_**example.bin**_"
## Recording leakage traces
In this stage, the "_**.bin**_" file (which is already generated
in the [previous section](#compiling-the-target-program))
is used as the input of [GILES](https://github.com/sca-research/GILES).
Before recording the leakage traces, it is necessary to copy/paste
[_**coeffs.json**_ file](https://github.com/sca-research/GILES/blob/master/coeffs.json)
into the "_**example**_" folder (The "_**coeffs.json**_" file can
be found in [GILES page](https://github.com/sca-research/GILES) or
in this repository).

Now, as [GILES](https://github.com/sca-research/GILES)
is already installed in [this subsection](#installing-giles) 
for measuring leakage traces, run the below command
from the directory where the "_**example.bin**_" file is 
there ("_**example**_" folder):

`GILES example.bin -r NUM -o name_trs.trs`

In this command, there are some flags as below:

1) `example.bin`: The compiled targeted program.
2) `-r NUM`: The number of traces/the times that 
targeted program would be run. **Note:** In each run, the **Plaintext** 
   is generated randomly
   (see "**main.c**" in "**Masked_Combined_AES**" folder).
   
3) `-o name_trs.trs`: This flag generates the output of
   [GILES](https://github.com/sca-research/GILES)
in the format
   ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/).
 Hence, all leakage traces and information 
   (Plaintexts, Ciphertext, ...)
   are automatically stored in  
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
   file.

4) There is no need to specify the leakage model, because the 
   default leakage model is [Hamming Weight](https://en.wikipedia.org/wiki/Hamming_Weight) 
model.
## Analysing recorded traces and data in a _trs_ file
The output of [GILES](https://github.com/sca-research/GILES)
is a file with
   ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/), a 
set file so-called **trs file**
which is a standard format defined by
   [Riscure's Inspector](https://www.riscure.com/security-tools/inspector-sca/).


### Construction of a trs file
  A short brief from [here](https://trsfile.readthedocs.io/en/latest/api.html),
  a ["_**.trs**_"]((https://trsfile.readthedocs.io/en/latest/)
  ) file contains a Specific storage engine
  (Engine), and the **Engine** composed some **Headers** 
  and **Padding_mode**, etc.

In this project, the **Headers** section is used which 
includes some information such as:  
+ Number of traces
+ Number and value of samples of each trace
+ Cryptographic information such as Plaintext, Ciphertext, ...
+ ...

 The below figure gives an overview of
 ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/):


                                                     **trs file**

                         +-----------------------------------------------------------------------+
                         |                           Specific storage engine                     |
                         +-----------------------------------------------------------------------+
                                                             |
                                                             |
                                                             V
                             +--------------------+--------------------+--------------------+
                             |       Headers      |      Live_update   |    Padding_mode    |
                             +--------------------+--------------------+--------------------+
                                         |
                                         |
                                         V
                                 +--------------+--------------+--------------+------
                                 |    HEADER1   |    HEADER2   |    HEADER3   |   ...
                                 +--------------+--------------+--------------+------
                                         |              |               |
                                         |              |               |---> Cryptographic information 
                                         |              |
                                         |              |---> Number of samples of each trace
                                         |
                                         |---> Number of traces 

### Reading the content of a trs file
To open and read a ["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/) 
file as well as extract the desired data from that,
[Riscure's Inspector](https://www.riscure.com/security-tools/inspector-sca/)
provides a library in [_Python_](https://pypi.org/project/trs/)
so-called "_**trsfile**_".
In [this page](https://github.com/Riscure/python-trsfile)
some examples are given
related to reading and creating
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/).

There is a _**Python script**_ named "_**TRS.py**_" in the
"**Analysing_recorded_traces**" folder. This script uses
["_**trsfile**_"](https://github.com/Riscure/python-trsfile) module
for extracting the information stored in 
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/).
This script reads a 
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
file, plots all leakage traces and also prints cryptographic data
(Plaintext and Ciphertext). So, the content of  
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
generated by [GILES](https://github.com/sca-research/GILES)
can be analysed through this script.




## DPA attacks
All the Differential Power Analysis (DPA) attacks are performed 
on
[Masked_Combine AES](#masked-combined-aes-for-arm-cortex-m0) that target
the output of S_Box in the first round of encryption. 
So, for specifying the first round,
the 21-th line in "_**Masked_Combined.c**_" should be 
`    for(round = 0; round < 1; round++) {` 
not 
`    for(round = 0; round < 10; round++) {` which is for all 10 rounds. 
In these attacks, the prediction function for guessing the key is 
[Hamming Weight](https://en.wikipedia.org/wiki/Hamming_Weight)
model. 
Furthermore, the highest value of 
**Pearson's Correlation coefficient** related to key guesses 
reveals the correct key.

All leakage traces are measured by
[GILES](https://github.com/sca-research/GILES) 
and stored in a 
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/)
### First-order DPA attack
In the "**1_O_dpa_pytrs**" and "**1_O_dpa_trsfile**" folders, 
the first-order DPA attacks on **Unmasked_Combined AES** are performed
in _**Python scripts**_. **Unmasked_Combined AES** means that for 
the [target program](#masked-combined-aes-for-arm-cortex-m0), the
corresponding value of
`NUM_SHARES` in the "_**masked_combined.h**_" file is **1 (ONE)**.

The only difference between 
"**1_O_dpa_pytrs**" and "**1_O_dpa_trsfile**" attacks is
the module that they use in order to read 
and also extract the data from
["_**.trs**_"](https://trsfile.readthedocs.io/en/latest/).
"**1_O_dpa_pytrs**" gains [pytrs module](https://github.com/sca-research/PyMod4Trs)
"**1_O_dpa_trsfile**" uses [trsfile module](https://github.com/Riscure/python-trsfile)


### Second-order DPA attack
In the "**2_O_dpa_trsfile**" folder, 
the second-order DPA attacks on **Masked_Combined AES** are performed
in _**Python scripts**_. In **Masked_Combined AES** 
[target program](#masked-combined-aes-for-arm-cortex-m0), the value of
`NUM_SHARES` in the "_**masked_combined.h**_" file is **2 (TWO)**.
For the second-order DPA attacks
two combination functions **Centered_Product** and 
**Centered_Absolute_Difference**[1] are used. 
Also, there is a comparison between the results of these 
two functions.

## References

[1] P.R.B: “Statistical analysis of second order differential power analysis,”IEEE Transactions on computers 2009"
[2] "Faster Evaluation of SBoxes via Common Shares"
[3] "Further Improving Efficiency of Higher-Order Masking Schemes by Decreasing Randomness Complexity"
