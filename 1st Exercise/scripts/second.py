from numpy import *
from matplotlib import pyplot as plt
fn = "../data/data_provinces.csv"
#arange(# of columns)+displacement from the left<- for the column
#dtype = a is string
name = loadtxt(fn, unpack = True, delimiter = ",", skiprows=1, usecols = arange(1), dtype = 'a') 
region = loadtxt(fn, unpack = True, delimiter = ",", skiprows=1, usecols = arange(1)+1, dtype = 'a')
population, lifeExpectancy ,\
incomePerCapita,expenditurePerCapita \
=loadtxt(fn,unpack=True, delimiter=",", skiprows=1, usecols = arange(4)+2)

region_list=unique(region)

color_list=array(['red', 'blue', 'green','red', 'blue', 'green','red', 'blue', 'green', 'red', 'blue', 'green','red', 'blue', 'green','red', 'blue'])
colors=zeros(len(name),dtype='a') #zeros will make an array with zeroes as contents

for i in arange(len(name)):
    #array nasa numpy
    colors[i]=color_list[region_list==region[i]][0] #gets the zero

##s=size of circle
##alpha = transparency
##c = color        
                        
plt.clf()
plt.scatter(incomePerCapita, lifeExpectancy, s=population/min(population)*20, alpha=0.5, c=colors)
plt.show()

#argsort() = sorts list but does not change the list itself. 

