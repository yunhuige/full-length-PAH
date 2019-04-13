import sys, os
import numpy as np
from matplotlib import pyplot as plt

colors=['black','red','green','yellow','cyan','blue','magenta','orange','indigo','pink','darkred','indianred','springgreen','purple','goldenrod','peru','y','lightskyblue','blueviolet','gold','lightgreen','deeppink','darkorchid','navy']

time = np.load('time.npy')
f1=np.load('f1.npy')
f2=np.load('f2.npy')
f3=np.load('f3.npy')
f4=np.load('f4.npy')
d1=np.load('d1.npy')
d2=np.load('d2.npy')
d3=np.load('d3.npy')
d4=np.load('d4.npy')

plt.figure(figsize=(12,12))
plt.subplot(4,1,1)
for i in range(11):
    plt.plot(d1[i],f1[i],color=colors[i])
plt.xlabel('position (nm)')
plt.ylabel('Force (kJ/mol/nm)')

plt.subplot(4,1,2)
for i in range(11):
    plt.plot(d2[i],f2[i],color=colors[i])
plt.xlabel('position (nm)')
plt.ylabel('Force (kJ/mol/nm)')

plt.subplot(4,1,3)
for i in range(11):
    plt.plot(d3[i],f3[i],color=colors[i])
plt.xlabel('position (nm)')
plt.ylabel('Force (kJ/mol/nm)')

plt.subplot(4,1,4)
for i in range(11):
    plt.plot(d4[i],f4[i],color=colors[i])
plt.xlabel('position (nm)')
plt.ylabel('Force (kJ/mol/nm)')

plt.tight_layout()
plt.savefig('force_dis.pdf')

