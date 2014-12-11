from numpy import *
from matplotlib import pylab as plt

#xvar = array([1,2,3,4,5])
#yvar = xvar*2
#yvar2 = xvar*4

xvar, yvar = loadtxt("../data/data.csv", unpack = True, delimiter = ",")

plt.clf()
plt.plot(xvar,yvar,'rx')
#plt.plot(xvar,yvar2,'rx')

plt.xlim((0,6))
plt.ylim((0,12))

plt.xlabel("variable X")
plt.ylabel("variable Y")
plt.show()
plt.title("My First Python Plot")
#plt.savefig("../figures/fig_first_plot2.png")