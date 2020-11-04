import TRS_Reader # Si Gao ---> https://github.com/gs1989/DPAdemo
import matplotlib.pyplot as plt


def x_axis(r1, r2):
    return [item for item in range(r1, r2+1)]

# the number of encryption in main.c
#i=number_of_encryption
trs = TRS_Reader.TRS_Reader('trs1.trs')
trs.read_header()
trs.read_traces()
fig, ax = plt.subplots()

# Iterate over the first 25 traces
for i  in range(trs.Number_of_Traces):
    print('Trace {0:d} contains {1:d} samples'.format(i, trs.number_of_samples))
    print('  - minimum value in trace: {0:f}'.format(min(trs.traces[i])))
    print('  - maximum value in trace: {0:f}'.format(max(trs.traces[i])))
    y_data =[trs.traces[i,j] for j in range(len(trs.traces[i]))]
    x_data = x_axis(1, len(y_data[4:9]))
    ax.plot(x_data, y_data[4:9])
    print("Plaintext=")
    for j in range(int(trs.cryptolen/2)):
        print("{0}".format(trs.plaintext[:,j]))
    print("\n")

    print("Ciphertext=")
    for j in range(int(trs.cryptolen/2)):
        print("{0}".format(trs.ciphertext[i,j]))
    print("\n")

ax.set(xlabel='Samples', ylabel='Amplitude(HW)',title='GILES')
ax.grid()
#fig.savefig("GILES2.png")
plt.show()

