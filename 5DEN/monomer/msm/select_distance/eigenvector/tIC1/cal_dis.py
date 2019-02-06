import sys, os
import mdtraj as md
import numpy as np

ind=np.array([[1227,6884],[1295,6817],[6542,818],[6543,817],[6559,818],[1346,6600]])
#a=np.arange(0,528,1)
#b=np.delete(a,(73))
dis1=[]
dis2=[]
dis3=[]
dis4=[]
dis5=[]
dis6=[]
for i in range(998):
        print i
        t=md.load('../../traj%d.xtc'%i,top='../../14121.gro')
        d=md.compute_distances(t,ind,periodic=True)
        for j in range(len(d)):
                dis1.append(d[j][0])
                dis2.append(d[j][1])
                dis3.append(d[j][2])
                dis4.append(d[j][3])
		dis5.append(d[j][4])
		dis6.append(d[j][5])
np.save('0.npy',dis1)
np.save('1.npy',dis2)
np.save('2.npy',dis3)
np.save('3.npy',dis4)
np.save('4.npy',dis5)
np.save('5.npy',dis6)
