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

system = top.createSystem(nonbondedMethod=PME,nonbondedCutoff=1*nanometer, constraints=HBonds) #create the system
integrator = openmm.LangevinIntegrator(300*unit.kelvin, 1.0/unit.picoseconds, timestep)

platform = Platform.getPlatformByName("CUDA")
properties={'CudaPrecision': 'mixed'}
simulation = Simulation(top.topology, system, integrator,platform, properties)  

print ("running job %d"%run)

if os.path.isfile("checkpnt_free_%d.chk"%(int(run)-1)):
      print ("running job%d, no minimization, and loading chkpnt from job%d"%(run,int(run)-1))
      with open('checkpnt_free_%d.chk'%(int(run)-1), 'rb') as f:
           simulation.context.loadCheckpoint(f.read())     
else:
     print ("working on minimization, loading the last frame of previous run")
     with open('state%d.xml'%(int(run)-1), 'r') as f:
          state = openmm.XmlSerializer.deserialize(f.read())
     print ("generating new velovity from last frame of previours run")
     simulation.context.setState(state)
     simulation.context.setVelocitiesToTemperature(temperature)
     simulation.minimizeEnergy()
      
print("Appending reporters...")
simulation.reporters.append(app.DCDReporter('mtd_%d.dcd'%run, 5000)) #10ps 
simulation.reporters.append(StateDataReporter(stdout, 5000, speed=True,step=True,
        potentialEnergy=True, temperature=True))
simulation.reporters.append(StateDataReporter('output%d.log'%run, 5000, speed=True,step=True, time = True, potentialEnergy = True, temperature = True, kineticEnergy=True, separator='\t'))
simulation.reporters.append(CheckpointReporter('checkpnt_free_%d.chk'%run, 5000))

simulation.step(100000) #200ps


#getting the last frame coordinate.
state=simulation.context.getState(getPositions=True)
#print (state)
with open('state%d.xml'%run, 'w') as f:
     f.write(openmm.XmlSerializer.serialize(state))
print('saved state.xml')

print("Done!")
