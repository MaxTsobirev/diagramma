import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.subplots()
plt.grid(axis="x", color="green", alpha=3, linewidth=5, linestyle=":")
plt.grid(True)

x1=np.arange(-9,0,1)
x2=np.arange(1,10,1)
x3=np.arange(-9,0,1)
x4=np.arange(1,10,1)
x5=np.arange(-9,-5,0.5)
x6=np.arange(6,10,1)
x7=np.arange(-1,2,1)

y1=(-1/16)*(x1+5)**2+2
y2=(-1/16)*(x2-5)**2+2
y3=(1/4)*(x3+5)**2-3
y4=(1/4)*(x4-5)**2-3
y5=-1*(x5+7)**2+5
y6=-1*(x6-7)**2+5
y7=(-0.5)*x7**2+1.5

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
plt.show()

