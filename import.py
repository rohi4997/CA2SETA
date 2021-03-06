import matplotlib.pyplot as plt
import math
from array import *

x = array('f', [])
y = array('f', [])
h = 6.62e-34
k = 1.38e-23
c = 3e8
T = 5000
ld = 2e-7
while (T<=4000):
    for i in range(200):
    r = ((8*math.pi*h*c)/math.pow(ld, 5))*(1/(math.exp((h*c)/(ld*k*T)) -1))
    x.append(ld)
    y.append(r)
    ld += 0.2e-7
    T += 4000



plt.plot(x, y)
plt.xlabel('Wavelength')
plt.ylabel('Spectral energy density')
plt.title('Blackbody Radiation')
plt.show()