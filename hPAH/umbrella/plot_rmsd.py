import sys, os
import numpy as np
from matplotlib import pyplot as plt


k = [100,150,200]
label=['A1','A2','A3','A4','C1','C2','C3','C4']

colors=['black','red','green','yellow','cyan','blue','magenta','orange','indigo','pink','darkred','indianred','springgreen','purple','goldenrod','peru','y','lightskyblue','blueviolet','gold','lightgreen','deeppink','darkorchid','navy']

plt.figure(figsize=(12,12))
for i in range(len(k)):
    print k[i]
    dis = np.load('rmsd_%dkJ.npy'%k[i])
    time = np.arange(0,len(dis[0])*10.,10.)
    plt.subplot(len(k),1,i+1)
    for j in range(len(dis)):
        print j
        plt.plot(time,dis[j],color=colors[j],label=label[j])
    plt.xlabel('time (ps)')
    plt.ylabel('rmsd (nm)')
    plt.legend(loc='best',fontsize=6)
    plt.title('%d (kJ/mol/nm)'%k[i])
plt.tight_layout()
plt.savefig('rmsd.pdf')    

    


