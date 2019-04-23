import sys, os
import mdtraj as md
import numpy as np


t1 = md.load('new.gro')
t2 = md.load('full_xtal.gro')

atom = ['CA','N','O','C','CB']

for i in range(4):
    for j in range(len(atom)):
        new_ind = []
        ind = t1.topology.select('((index 312 to 417) or (index 474 to 898) or (index 948 to 1312) or (index 1347 to 1641) or (index 1659 to 2190) or (index 2274 to 7172)) and (name == %s)'%atom[j])
        ind2 = t2.topology.select('(index 0 to 2019) and (name == %s)'%atom[j])
        if len(ind) == len(ind2):
            for k in range(len(ind)):
                new_ind.append([ind[k]+i*7287,ind2[k]+i*2020])
        else:
            raise ValueError('check length')
        np.save('ind_%d_%s.npy'%(i,atom[j]),new_ind)


