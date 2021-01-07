from scipy import fft
import math
from matplotlib import pyplot as plt

data = [15, 16, 15, 14, 13, 12, 15, 18, 18, 19, 18, 19, 18, 19, 20, 20, 21, 21, 21, 21, 22, 24, 24]
n = len(data)
m = n-1
mean = sum(data)/n
spect = []
corel = []


def find_corel(k,l1, l2):
    temp = 0
    for x,y in zip(l1,l2):
        temp += (x-mean) * (y-mean)
    c = temp/k
    corel.append(c)
    

for t in range(n):
    l1 = data[0:n-t]
    l2 = data[t:n]
    find_corel(n-t,l1,l2)


cosine = fft.dct(corel)

spectral = []

spec = list(rel*(-1)**n for (n,rel) in zip(range(1,m),cosine[1:m]))


spectral.append(((cosine[0]+cosine[m])/(2*m)) + (sum(cosine[1:m]))/m)
for k in range(1,m):
    temp = 0
    for x in range(1,m):
        temp+= cosine[x]*(math.cos(math.pi*k*x/m))
    spectral.append(((cosine[0]+(cosine[m]*(-1)**k))/(2*m)) + (1/m)*(temp))

smooth = []
m=m-1

smooth.append(spectral[0]*0.5+spectral[1]*0.5)
for k in range(1,m):
    smooth.append((spectral[k-1]+spectral[k+1])*0.25+spectral[k])
smooth.append(spectral[m]*0.5+spectral[m-1]*0.5)

plt.plot(range(0,n-1), smooth)
plt.plot(range(0,n), data)
plt.show()



