import sys, os
import mdtraj as md
import numpy as np


t1 = md.load('new.gro')
t2 = md.load('full_xtal.gro')

atom = ['CA','N','O','C','CB']

for i in range(4):
    for j in range(len(atom)):
        new_ind = []
        ind = t1.topology.select('((index 312 to 417) or (index 474 to 898) or (index 948 to 1299) or (index 1334 to 1628) or (index 1646 to 2177) or (index 2261 to 7159)) and (name == %s)'%atom[j])
        ind2 = t2.topology.select('(index 0 to 2019) and (name == %s)'%atom[j])
        if len(ind) == len(ind2):
            for k in range(len(ind)):
                new_ind.append([ind[k]+i*7274,ind2[k]+i*2020])
        else:
            raise ValueError('check length')
        np.save('ind_%d_%s.npy'%(i,atom[j]),new_ind)


