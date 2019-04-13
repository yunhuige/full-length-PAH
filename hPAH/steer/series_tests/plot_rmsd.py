import sys, os
import numpy as np
from matplotlib import pyplot as plt

force = [10,20,30,40,50,60,70,80,90,100]

colors=['black','red','green','yellow','cyan','blue','magenta','orange','indigo','pink','darkred','indianred','springgreen','purple','goldenrod','peru','y','lightskyblue','blueviolet','gold','lightgreen','deeppink','darkorchid','navy']

for i in range(len(force)):
    print i
    rmsd_ACT = np.load('rmsd_%dkJ_ACT.npy'%force[i]) 
    rmsd_CAT = np.load('rmsd_%dkJ_CAT.npy'%force[i])
    time = np.arange(0,len(rmsd_ACT[0])*10.,10.)
    plt.figure(figsize=(12,12))
    for j in range(4):
        plt.subplot(4,1,j+1)
        plt.plot(time,rmsd_ACT[j],color=colors[j])
        plt.xlabel('time (ps)')
        plt.ylabel('rmsd (nm)')
    plt.title('RMSD ACT')
    plt.tight_layout()
    plt.savefig('rmsd_%dkJ_ACT.pdf'%force[i])
    plt.close()
    plt.figure(figsize=(12,12))
    for j in range(4):
        plt.subplot(4,1,j+1)
        plt.plot(time,rmsd_CAT[j],color=colors[j])
        plt.xlabel('time (ps)')
        plt.ylabel('rmsd (nm)')
    plt.title('RMSD CAT')
    plt.tight_layout()
    plt.savefig('rmsd_%dkJ_CAT.pdf'%force[i])
    plt.close()





