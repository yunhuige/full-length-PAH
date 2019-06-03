from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
#import metadynamics as mtd
from simtk import openmm, unit
import mdtraj as md 
import numpy as np 
import os,sys


input_gro=sys.argv[1]
input_top=sys.argv[2]


run=int(0)
while os.path.exists("checkpnt_mini_%d.chk"%run) or os.path.exists("checkpnt_all_%d.chk"%run) or os.path.exists("checkpnt_free_%d.chk"%run):
      run += 1

temperature = 300 * unit.kelvin
collision_rate=1.0 / unit.picosecond
timestep = 2.0 * unit.femtosecond

gro = GromacsGroFile(input_gro) #load .gro file--initial structure.
top = GromacsTopFile(input_top, periodicBoxVectors=gro.getPeriodicBoxVectors())
initial_state=gro.positions

ref_pdb= PDBFile('system_all_wt.pdb') #loading coordinates of references (only Ca atoms)


system = top.createSystem(nonbondedMethod=PME,nonbondedCutoff=1*nanometer, constraints=HBonds) #create the system



restraint_index=[]
restraint_ref_index=[]
for i in range(4):
    CA_index=np.load('../ind_%d_CA.npy'%i)
    C_index=np.load('../ind_%d_C.npy'%i)
    N_index=np.load('../ind_%d_N.npy'%i)
    O_index=np.load('../ind_%d_O.npy'%i)
    CB_index=np.load('../ind_%d_CB.npy'%i)

    restraint_index.append(CA_index[388:][:,0])
    restraint_index.append(C_index[388:][:,0])
    restraint_index.append(N_index[388:][:,0])
    restraint_index.append(O_index[388:][:,0])
    restraint_index.append(CB_index[369:][:,0])

    restraint_ref_index.append(CA_index[388:][:,1])
    restraint_ref_index.append(C_index[388:][:,1])
    restraint_ref_index.append(N_index[388:][:,1])
    restraint_ref_index.append(O_index[388:][:,1])
    restraint_ref_index.append(CB_index[369:][:,1])



restraint_index=np.concatenate(restraint_index)
restraint_ref_index=np.concatenate(restraint_ref_index)

restraint_index=[int(i) for i in restraint_index]
restraint_ref_index=[int(j) for j in restraint_ref_index]

referencePositions_all=gro.positions
"""using the xtal coordinates in refrecence postions"""
for index_index, index in enumerate(restraint_index):
    referencePositions_all[index]=ref_pdb.positions[restraint_ref_index[index_index]]
"""replace all the other coodinates with 000 vector"""
for i in range(len(referencePositions_all)):
    if i not in restraint_index:
       referencePositions_all[i]=[0,0,0]*nanometer

if run < 1 :
   K_RMSD = 0 * unit.kilocalories_per_mole / unit.angstroms**2
   RMSD0 = 0.00001 * unit.angstroms
   rmsd_cv=openmm.RMSDForce(referencePositions_all,restraint_index)
else:
   K_RMSD = 1200 * unit.kilocalories_per_mole / unit.angstroms**2
   RMSD0 = 0.00001 * unit.angstroms
   rmsd_cv=openmm.RMSDForce(referencePositions_all,restraint_index)

energy_expression = 'step(dRMSD) * (K_RMSD/2)*dRMSD^2; dRMSD = (RMSD-RMSD0);'
energy_expression += 'K_RMSD = %f;' % K_RMSD.value_in_unit_system(unit.md_unit_system)
energy_expression += 'RMSD0 = %f;' % RMSD0.value_in_unit_system(unit.md_unit_system)
restraint_force = openmm.CustomCVForce(energy_expression)
restraint_force.addCollectiveVariable('RMSD', rmsd_cv)
system.addForce(restraint_force)


integrator = openmm.LangevinIntegrator(300*unit.kelvin, 1.0/unit.picoseconds, timestep)


platform = Platform.getPlatformByName("CUDA")
properties={'CudaPrecision': 'mixed'}
simulation = Simulation(top.topology, system, integrator,platform, properties)  

print ("running job %d"%run)
if run < 1 :
   print ("doing minimization")
   gro = GromacsGroFile(input_gro) #load .gro file--initial structure.
#   simulation.context.setPositions(initial_state)
   simulation.context.setPositions(gro.positions)
   simulation.minimizeEnergy()

else:
   print ("loding previous %d.chk file"%(int(run)-1))
   with open('checkpnt_mini_%d.chk'%(int(run)-1), 'rb') as f:
        simulation.context.loadCheckpoint(f.read())


print("Appending reporters...")
simulation.reporters.append(app.DCDReporter('mtd_%d.dcd'%run, 5000)) #10ps 
simulation.reporters.append(StateDataReporter(stdout, 5000, speed=True,step=True,
        potentialEnergy=True, temperature=True))
simulation.reporters.append(StateDataReporter('output%d.log'%run, 5000, speed=True,step=True, time = True, potentialEnergy = True, temperature = True, kineticEnergy=True, separator='\t'))
simulation.reporters.append(CheckpointReporter('checkpnt_mini_%d.chk'%run, 5000))

#meta.step(simulation, 10000)
simulation.step(100000) #200ps

#getting the last frame coordinate.
state=simulation.context.getState(getPositions=True)
#print (state)
with open('state%d.xml'%run, 'w') as f:
     f.write(openmm.XmlSerializer.serialize(state))
print('saved state.xml')

print("Done!")
