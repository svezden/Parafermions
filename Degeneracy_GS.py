import numpy as np
import math
import matplotlib.pyplot as plt
import csv

''' Takes the output file and makes it a numpy.array. The string at the top of the file is
replaced by zeroes'''

with open('lowest_eigenvalues_6_15_tperp=0.2.txt','r') as data1:
    data_file = csv.reader(data1, delimiter='\n')
    data_array = np.zeros((42,10))
    i = 0
    for row in data_file:
        if i%42 == 0 or len(row)==0:
            data_array[i%42][int(i/42)]=0
        else:
            data_array[i%42][int(i/42)]=float(row[0])
        i +=1

with open('lowest_eigenvalues_6_11_tperp=0.txt','r') as data0:
    data_file = csv.reader(data0, delimiter='\n')
    data_array0 = np.zeros((42,6))
    i = 0
    for row in data_file:
        if i%42 == 0 or len(row)==0:
            data_array0[i%42][int(i/42)]=0
        else:
            data_array0[i%42][int(i/42)]=float(row[0])
        i +=1

n_sites =  np.array([5,6,7,8,9,10,11,12,13,14,15])

for i in range(2, 28):
    plt.plot(np.array([6,7,8,9,10,11]),data_array0[i][:]-data_array0[1][:],'bo')
plt.show()

#data for t_perp=0.1. Each row containd the three lowest eigenvalues of a particular length
data1 = np.array([
    [-1.046224898453263918e+01, -1.036743342893260333e+01, -1.027290728482459414e+01],
    [-1.313716802851307186e+01, -1.220244863032910487e+01, -1.218649108495520395e+01],
    [-1.530700834176110092e+01, -1.521623579159512829e+01, -1.512618553222648643e+01],
    [-1.776226381613874139e+01, -1.767082849449719717e+01, -1.757988806726514497e+01],
    [-2.033742003025989931e+01, -1.970466958582342798e+01, -1.968492358118713526e+01],
    [-2.260000879473314583e+01, -2.251174768411224747e+01, -2.242443191841643113e+01],
    [-2.260000879473314583e+01, -2.251174768411224747e+01, -2.242443191841643113e+01]])


#data for t_perp=0.2.
data2 =  np.array([
    [-1.055828302487650916e+01, -1.036861579566277847e+01, -1.018021621226039386e+01],
    [-1.313792364440938698e+01, -1.233890380499097716e+01, -1.228055879998623112e+01],
    [-1.539987940588557613e+01, -1.521803489865418868e+01, -1.503924851175760402e+01],
    [-1.785626523790532261e+01, -1.767347790982111633e+01, -1.749300451196124939e+01],
    [-2.033930121039912819e+01, -1.984684135571303898e+01, -1.977749996589874826e+01],
    [-2.269179357571443489e+01, -2.251510524972981386e+01, -2.234261379888567944e+01],
    [-2.512979294798012830e+01, -2.495232761293517854e+01, -2.477834558569444923e+01],
    [-2.756082109460230356e+01, -2.723840899703134255e+01, -2.716064652120526191e+01],
    [-2.996249695805717295e+01, -2.979003238501629269e+01, -2.962301327956630459e+01],
    [-3.239237543345269899e+01, -3.221931095472385209e+01, -3.205116570520197428e+01],
    [-3.479140049358603193e+01, -3.457715604380901198e+01, -3.449279143655686397e+01]])

n_sites =  np.array([5,6,7,8,9,10,11,12,13,14,15])
differences1 = [data1[i][0]-data1[i][2] for i in range(0,len(data1))]
differences2 = [data2[i][0]-data2[i][2] for i in range(0,len(data2))]

#plt.plot(n_sites[:-4],differences1)
#plt.plot(n_sites,differences2)
for i in range(2, 28):
    plt.plot(n_sites[1:],data_array[i][:]-data_array[1][:],'bx')
plt.show()
