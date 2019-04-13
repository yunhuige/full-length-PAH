import sys, os
import mdtraj as md
import numpy as np

force = [10,20,30,40,50,60,70,80,90,100]

t = md.load('protein.gro')
ind1 = t.topology.select("(index 460 to 1879) and (backbone or (name == 'CB'))") 
ind2 = t.topology.select("(index 1880 to 6602) and (backbone or (name == 'CB'))")
ind_ACT = []
ind_CAT = []
for i in range(4):
    ind_ACT.append(ind1+i*7291)
    ind_CAT.append(ind2+i*7291)

for i in range(len(force)):
    print i
    rmsd_ACT=[]
    rmsd_CAT=[]
    traj=md.load('%dkJ/RUN0/traj_comp.xtc'%force[i],top='%dkJ/RUN0/protein.gro'%force[i])
    ref = traj[0]
    for j in range(4):
        ACT = traj.atom_slice(ind_ACT[j])
        ACT_ref = ref.atom_slice(ind_ACT[j])
        CAT =traj.atom_slice(ind_CAT[j])
        CAT_ref = ref.atom_slice(ind_CAT[j])
        r_ACT = md.rmsd(ACT,ACT_ref)
        r_CAT = md.rmsd(CAT,CAT_ref)
        rmsd_ACT.append(r_ACT)
        rmsd_CAT.append(r_CAT)
    np.save('rmsd_%dkJ_ACT.npy'%force[i],rmsd_ACT)
    np.save('rmsd_%dkJ_CAT.npy'%force[i],rmsd_CAT)


