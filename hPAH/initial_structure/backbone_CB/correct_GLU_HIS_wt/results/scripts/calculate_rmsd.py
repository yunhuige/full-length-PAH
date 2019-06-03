import mdtraj as md
import numpy as np
import os,sys,glob


dcds = glob.glob("*.chk")


#ref_pdb= md.load('../system_all_wt.pdb')
#restraint_index=[]
#for i in range(11,270):
#    restraint_index.append(i)

restraint_index=[]
restraint_ref_index=[]
for i in range(4):
    CA_index=np.load('../ind_%d_CA.npy'%i)
    C_index=np.load('../ind_%d_C.npy'%i)
    N_index=np.load('../ind_%d_N.npy'%i)
    O_index=np.load('../ind_%d_O.npy'%i)
    CB_index=np.load('../ind_%d_CB.npy'%i)

    restraint_index.append(CA_index[:,0])
    restraint_index.append(C_index[:,0])
    restraint_index.append(N_index[:,0])
    restraint_index.append(O_index[:,0])
    restraint_index.append(CB_index[:,0])

    restraint_ref_index.append(CA_index[:,1])
    restraint_ref_index.append(C_index[:,1])
    restraint_ref_index.append(N_index[:,1])
    restraint_ref_index.append(O_index[:,1])
    restraint_ref_index.append(CB_index[:,1])

restraint_index=np.concatenate(restraint_index)
restraint_ref_index=np.concatenate(restraint_ref_index)

for i in range(len(dcds)):
#for i in range(23):
    print ("working on traj%d"%i)
    traj_whole=md.load('mtd_%d.dcd'%i,top='../solv_ions.gro')
#    traj_whole.save('mtd_whole_%d.dcd'%i)

#    cacb_inds = traj_whole[0].topology.select('name==CA or name==CB')
#    _inds=restraint_index
#    spliced_trajs=traj_whole.atom_slice(cacb_inds)
    spliced_trajs=traj_whole.atom_slice(restraint_index)

    ref_subatoms=md.load('system_all_wt.pdb').atom_slice(restraint_ref_index)

    rmsd_results=md.rmsd(spliced_trajs,ref_subatoms)
    print (rmsd_results)
    np.save('rmsd_traj%d.npy'%i,rmsd_results)

print ("done")

