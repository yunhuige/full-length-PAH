import sys, os
import mdtraj as md

t = md.load('mtd_50.dcd',top='../solv_ions.pdb')
t2 = t.image_molecules(inplace=False)
t2.save_dcd('mtd_50_pbc.dcd')
t2.center_coordinates()
t2.save_dcd('mtd_50_pbc_center.dcd')
