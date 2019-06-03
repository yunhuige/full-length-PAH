import sys, os
import mdtraj as md



f =[5,20,50]

#for i in f:
for i in range(21,51):
	a = md.load('mtd_%d.dcd'%i,top='../solv_ions.gro')
	a[-1].save_gro('%d.gro'%i)
	t=md.load('%d.gro'%i)
	t.remove_solvent(inplace=True)
	t.save_gro('%d_protein.gro'%i)


