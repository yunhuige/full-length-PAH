import sys, os
import numpy as np
from matplotlib import pyplot as plt
force = [10,20,30,40,50,60,70,80,90,100]
time=[[[] for i in range(len(force))] for j in range(4)]
f = [[[]for i in range(len(force))] for j in range(4)]
d = [[[]for i in range(len(force))] for j in range(4)]
w = [[[]for i in range(len(force))] for j in range(4)]
#print f
#sys.exit()
#f1=[[] for i in range(len(force))]
#f2=[[] for i in range(len(force))]
#f3=[[] for i in range(len(force))]
#f4=[[] for i in range(len(force))]

colors=['black','red','green','yellow','cyan','blue','magenta','orange','indigo','pink','darkred','indianred','springgreen','purple','goldenrod','peru','y','lightskyblue','blueviolet','gold','lightgreen','deeppink','darkorchid','navy']

for i in range(len(force)):
    filename='%dkJ/RUN0/pullf.xvg'%force[i]
    with open(filename) as fi:
        lines=fi.readlines()
    for k in range(len(lines)):
        if lines[k][0] != '@' and lines[k][0] != '#':
            n = k
            break
    for j in range(n,len(lines)):
        for l in range(4):
            time[l][i].append(float(lines[j].split()[0]))
            f[l][i].append(float(lines[j].split()[int(l+1)]))

for i in range(len(force)):
    plt.figure(figsize=(12,12))
    for j in range(4):
        plt.subplot(4,1,j+1)
        plt.plot(time[j][i],f[j][i],color=colors[j])
        plt.xlabel('time (ps)')
        plt.ylabel('Force (kJ/mol/nm)')
    plt.tight_layout()
    plt.savefig('force_%dkj.pdf'%(force[i]))
    plt.close()

for i in range(len(force)):
    filename='%dkJ/RUN0/pullx.xvg'%force[i]
    with open(filename) as fi:
        lines=fi.readlines()
    for k in range(len(lines)):
        if lines[k][0] != '@' and lines[k][0] != '#':
            n = k
            break
    for j in range(n,len(lines)):
        for l in range(4):
            d[l][i].append(float(lines[j].split()[int(l+1)]))
np.save('time.npy',time)
np.save('force.npy',f)
np.save('distance.npy',d)
for i in range(len(force)):
    plt.figure(figsize=(12,12))
    for j in range(4):
        plt.subplot(4,1,j+1)
        plt.plot(time[j][i],d[j][i],color=colors[j])
        plt.xlabel('time (ps)')
        plt.ylabel('position (nm)')
    plt.tight_layout()
    plt.savefig('dis_%dkj.pdf'%(force[i]))
    plt.close()

for i in range(len(force)):
    for j in range(4):
        for k in range(len(d[j][i])):
            w[j][i].append(d[j][i][k]*f[j][i][k])

for i in range(len(force)):
    plt.figure(figsize=(12,12))
    for j in range(4):
        plt.subplot(4,1,j+1)
        plt.plot(time[j][i],w[j][i],color=colors[j])
        plt.xlabel('time (ps)')
        plt.ylabel('work (kJ/mol)')
    plt.tight_layout()
    plt.savefig('work_%dkj.pdf'%(force[i]))
    plt.close()



