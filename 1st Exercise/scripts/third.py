from numpy import *
from matplotlib import pyplot as plt
fn = "../data/data_provinces.csv"

name = loadtxt(fn, unpack = True, delimiter = ",", skiprows=1, usecols = arange(1), dtype = 'a') 
region = loadtxt(fn, unpack = True, delimiter = ",", skiprows=1, usecols = arange(1)+1, dtype = 'a')
population, lifeExpectancy ,\
incomePerCapita,expenditurePerCapita \
=loadtxt(fn,unpack=True, delimiter=",", skiprows=1, usecols = arange(4)+2)

#Group by region then sum the population of the provinces belonging to that region
regionList = unique(region)
regionPopulationList = zeros(len(regionList),dtype='i')
for i in arange(len(name)):
    regionPopulationList[region[i] == regionList] += population[i] 
regionPopulationArranged = argsort(regionPopulationList)
for i in arange(len(regionList)):
    print "%s : %.2f" %(regionList[regionPopulationArranged][i], regionPopulationList[regionPopulationArranged][i]/1e6)
    
plt.clf()
plt.ylabel("Regions")
plt.xlabel("Population (in Millions)")
plt.barh(arange(len(regionList)),regionPopulationList[regionPopulationArranged]/1e6, height = 0.8, left = None )
plt.yticks(arange(len(regionList)), regionList[regionPopulationArranged])
plt.show()

#Group by region then get the average lifeExpectancy of that region
regionLifeExList = zeros(len(regionList),dtype='f')
provincesCount = zeros(len(regionList),dtype='i')
for i in arange(len(name)):
    regionLifeExList[region[i] == regionList] += lifeExpectancy[i]
    provincesCount[region[i] == regionList] += 1
for i in arange(len(regionLifeExList)):
    regionLifeExList[i] /= provincesCount[i]
    
regionLifeExArranged = argsort(regionLifeExList)
for i in arange(len(regionLifeExList)):
    print "%s : %.2f" %(regionList[regionLifeExArranged][i], regionLifeExList[regionLifeExArranged][i])

#plt.clf()
#plt.ylabel("Regions")
#plt.xlabel("Average Life Expectancy (in Years)")
#plt.barh(arange(len(regionList)),regionLifeExList[regionLifeExArranged], height = 0.8, left = None )
#plt.yticks(arange(len(regionList)), regionList[regionLifeExArranged])
#plt.show()
