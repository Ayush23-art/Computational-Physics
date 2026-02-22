import numpy as np 
import matplotlib.pyplot as plt 

def f(r):
    #return the density of the disc
    return 2*np.pi*r*np.sqrt(r)

R = 4 # radius of disc
N = 100 # max. number of partitions

# for each value of number of partitions, store the value of integral in another array called I. 
#============
h = []
er = []
n = 1
while(n<=N):
    hn = R/n
    h.append(hn)
    dn = 0
    up = hn
    area = 0
    i = 0
    while(i<n):
        area = area+0.5*(f(up)+f(dn))*hn
        dn = up
        up = up+hn
        i = i+1
    er.append(np.abs(128*np.pi/5 -area))
    n = n+1



#============
# Calculate the error
# er = np.abs(128*np.pi/5 -I)
# the slope of the log-log plot is the exponent
slope = (np.log10(er[30]) - np.log10(er[60]))/(np.log10(h[30]) - np.log10(h[60]))
print(slope)

# Plot the error versus step size h
plt.loglog(h,er)
plt.xlabel("h")
plt.ylabel("Error")
plt.grid()
plt.show()
