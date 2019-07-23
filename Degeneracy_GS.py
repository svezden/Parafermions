import numpy as np
import math
import matplotlib.pyplot as plt
import csv
import argparse
from scipy.optimize import curve_fit


''' Takes the output file and makes it a numpy.array. The string at the top of the file is
replaced by zeroes'''

def file_to_array(a):
    with open(a,'r') as data:
        data_file = csv.reader(data, delimiter='\n')
        data_array = np.zeros((42,11))
        i = 0
        for row in data_file:
            if i%42 == 0 or len(row)==0:
                data_array[i%42][int(i/42)]=0
            else:
                data_array[i%42][int(i/42)]=float(row[0])
            i +=1
    return data_array

n_sites =  np.array([5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.])

#The spectrum of the system is similar for lengths related by three, so
# we separate the different lengths by color

# Taking input files from console
parser = argparse.ArgumentParser(description='Files to be plotted.')
parser.add_argument("files",nargs = 25, type =str)
args = parser.parse_args()

for i in range(0,len(args.files)):
    file_ = str(args.files[i])
    data_array = file_to_array(file_)
    plt.subplot(5,5,i+1)
    for j in range(1, 41):
        plt.plot(np.array([[5,8,11]]),data_array[j:j+1,[0,3,6,9]]-data_array[1:2,[0,3,6,9]],'r.')
    for j in range(1, 41):
        plt.plot(np.array([[6,9,12]]),data_array[j:j+1,[1,4,7,10]]-data_array[1:2,[1,4,7,10]],'g.')
    for j in range(1, 41):
        plt.plot(np.array([[7,10]]),data_array[j:j+1,[2,5,8]]-data_array[1:2,[2,5,8]],'b.')
        plt.title(file_)
    
# Fitting Exponential function for t_perp 0.1
def exp_fit(x,a,b,c):
    return a*np.exp(-b*(x-5.))+c
# Fitting power law function
def power_law_fit(x,a,b,c):
    return a*x**(-b)+c

ydata = data_array[28][:]-data_array[1][:]

popt, pcov = curve_fit(power_law_fit, n_sites, ydata, bounds=([2,0.5,0],[20,3.,2]))
#plt.plot(n_sites,power_law_fit(n_sites,*popt),'r-')

popt_exp, pcov_exp = curve_fit(exp_fit, n_sites, ydata, bounds=([0.2,.01,0.],[5,2.,1.]))
#plt.plot(n_sites,exp_fit(n_sites,*popt_exp),'b-')

#plt.ylim(-0.1,5)
#plt.xlim(4.8,15.1)
#print(popt_exp)
#print(popt)

plt.tight_layout()
plt.show()
