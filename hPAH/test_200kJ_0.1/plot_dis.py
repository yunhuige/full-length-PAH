import sys, os
import numpy as np
from matplotlib import pyplot as plt
time=[[] for i in range(11)]
f1=[[] for i in range(11)]
f2=[[] for i in range(11)]
f3=[[] for i in range(11)]
f4=[[] for i in range(11)]

colors=['black','red','green','yellow','cyan','blue','magenta','orange','indigo','pink','darkred','indianred','springgreen','purple','goldenrod','peru','y','lightskyblue','blueviolet','gold','lightgreen','deeppink','darkorchid','navy']

for i in range(11):
    filename='RUN%d/pullx.xvg'%i
    with open(filename) as f:
        lines=f.readlines()
    for k in range(len(lines)):
        if lines[k][0] != '@' and lines[k][0] != '#':
            n = k
            break
    for j in range(n,len(lines)):
        time[i].append(float(lines[j].split()[0]))
        f1[i].append(float(lines[j].split()[1]))
        f2[i].append(float(lines[j].split()[2]))
        f3[i].append(float(lines[j].split()[3]))
        f4[i].append(float(lines[j].split()[4]))
np.save('time.npy',time)
np.save('d1.npy',f1)
np.save('d2.npy',f2)
np.save('d3.npy',f3)
np.save('d4.npy',f4)

plt.figure(figsize=(12,12))
plt.subplot(4,1,1)
for i in range(11):
    plt.plot(time[i],f1[i],color=colors[i])
plt.xlabel('time (ps)')
plt.ylabel('position (nm)')

plt.subplot(4,1,2)
for i in range(11):
    plt.plot(time[i],f2[i],color=colors[i])
plt.xlabel('time (ps)')
plt.ylabel('position (nm)')

plt.subplot(4,1,3)
for i in range(11):
    plt.plot(time[i],f3[i],color=colors[i])
plt.xlabel('time (ps)')
plt.ylabel('position (nm)')

plt.subplot(4,1,4)
for i in range(11):
    plt.plot(time[i],f4[i],color=colors[i])
plt.xlabel('time (ps)')
plt.ylabel('position (nm)')

plt.tight_layout()
plt.savefig('dis_fig.pdf')

