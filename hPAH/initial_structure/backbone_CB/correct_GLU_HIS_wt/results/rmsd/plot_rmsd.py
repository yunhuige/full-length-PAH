import sys, os
import numpy as np
from matplotlib import pyplot as plt

rmsd = []
rmsd_mini = np.load('rmsd_traj0.npy')
rmsd_4helix = []
rmsd_all = []
rmsd_free = []

helix = range(1,6)
allr = range(6,21)
free = range(21,51)

for j in rmsd_mini:
    rmsd.append(j)    

for i in helix:
    r = np.load('rmsd_traj%d.npy'%i)
    for j in r:
        rmsd_4helix.append(j)
        rmsd.append(j)
for i in allr:
    r = np.load('rmsd_traj%d.npy'%i)
    for j in r:
        rmsd_all.append(j)
        rmsd.append(j)        
for i in free:
    r = np.load('rmsd_traj%d.npy'%i)
    for j in r:
        rmsd_free.append(j)
        rmsd.append(j)
#print len(rmsd_mini)
#print len(rmsd_4helix)
#print len(rmsd_all)
#print len(rmsd_free)
#print len(rmsd)
#sys.exit()

#time_mini = np.arange(10.,len(rmsd_mini)*10.+1.,10.)
#time_rmsd_4helix = np.arange(10.,len(rmsd_4helix)*10.+1.,10.) + len(rmsd_mini)*10.
#time_rmsd_all = np.arange(10.,len(rmsd_all)*10.+1.,10.) + len(rmsd_4helix)*10. + len(rmsd_mini)*10.
#time_rmsd_free = np.arange(10.,len(rmsd_free)*10.+1.,10.) + len(rmsd_4helix)*10. + len(rmsd_mini)*10. + len(rmsd_free)*10.

#print len(time_mini)
#print time_rmsd_4helix
#print time_rmsd_all
#print time_rmsd_free
#sys.exit()
time = np.arange(10,len(rmsd)*10.+1.,10.)
plt.figure(figsize=(30,10))
#plt.plot(time_mini,rmsd_mini,color='green',label='mini')
#plt.plot(time_rmsd_4helix,rmsd_4helix,color='red',label='4_helix')
#plt.plot(time_rmsd_all,rmsd_all,color='blue',label='all')
#plt.plot(time_rmsd_free,rmsd_free,color='black',label='free')
plt.plot(time[0:20],rmsd[0:20],color='green',label='mini')
plt.plot(time[19:120],rmsd[19:120],color='red',label='4_helix')
plt.plot(time[119:420],rmsd[119:420],color='blue',label='all')
plt.plot(time[419:],rmsd[419:],color='black',label='free')
plt.xlabel('time (ns)')
plt.ylabel('rmsd (nm)')
plt.xticks(range(0,12000,1000),range(0,12,1))
plt.legend(loc='lower right',fontsize=10)
plt.savefig('rmsd.pdf')
plt.show()



