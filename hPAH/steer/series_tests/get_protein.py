import sys, os

force = [10,20,30,40,50,60,70,80,90,100]

for i in range(len(force)):
    os.chdir('%dkJ/RUN0/'%force[i])
    os.system('echo "23\n" | gmx editconf -f solvent_ions_equilibrated2.gro -n index.ndx -o protein.gro')
    os.chdir('../../')
