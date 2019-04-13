import os, sys
import numpy as np

#rvalues1 = [(1.00 + i*0.5) for i in range(0,20)]
#rvalues += [(4.00 - i*0.1) for i in range(0,31)]
#print 'rvalues1', rvalues1
# write the mdp_files needed for these restraint values
#unique_rvalues1 = np.unique(np.array(rvalues1))

#print 'unique_rvalues1', unique_rvalues1
#sys.exit()
if not os.path.exists('mdp'):
    os.mkdir('mdp')

for r in range(10):
    mdp_text = """title                    = equil 
cpp                      = /lib/cpp
include                  = -I../top
define                   = 
integrator               = md-vv    ; sd not supported for expanded-ensemble!
dt                       = 0.002  ; 2 fs steps
nsteps                   = 1000000   ; 2 ns total
nstxout                  = 5000    ; every 100 ps
nstvout                  = 5000
nstlog                   = 5000
nstxtcout                = 5000 ; every 1 ps
nstcomm                  = 5000
comm_grps                = Protein  Non-Protein
xtc_grps                 = Protein
energygrps               = Protein  Non-Protein
nstlist                  = 10
;freezegrps               = r_1-298_&_C_N_O_CA
;freezedim                = Y Y Y
ns_type                  = grid
coulombtype     = PME
rvdw            = 0.9
rlist           = 0.9
rcoulomb        = 0.9
fourierspacing  = 0.12
pme_order       = 4
ewald_rtol      = 1e-5
fourierspacing           = 
pme_order                =
tcoupl                   = v-rescale
tc-grps                  = Protein Non-Protein
tau_t                    = 1.0  1.0  
ref_t                    = 300  300  
Pcoupl                   = no
tau_p                    = 1.0
compressibility          = 4.5e-5
ref_p                    = 1.0
gen_vel                  = yes
gen_temp                 = 300  
gen_seed                 = 173529  
constraints              = hbonds

cutoff-scheme = verlet    ; needed for gmx 5 !!!!!

; pulling parameters
; THR90_CA in protein, and ALA_CA in the ligand are the pull groups
; see: http://www.bevanlab.biochem.vt.edu/Pages/Personal/justin/gmx-tutorials/umbrella/05_pull.html

;;;;; Pull code for gmx 5.0.6 ;;;;;;;;;
pull                    = yes
pull_ngroups            = 16	;(1) The number of pull groups, not including the absolute reference group, when used.
                        	; Pull groups can be reused in multiple pull coordinates. Below only the pull options for
                        	; group 1 are given, further groups simply increase the group index number.
pull_ncoords            = 8
pull_group1_name        = ACT1
pull_group2_name        = CAT1
pull_coord1_geometry	        = distance      ; simple distance increase
pull_coord1_groups	= 1 2
pull_coord1_dim	        = Y Y Y		; all x,y,z components possible
pull_coord1_rate        = 0.10          ; 0.01 nm per ps = 10 nm per ns
pull_coord1_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord1_start              = no            ; yes           ; define initial COM distance > 0,
 					;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord1-init	= 3.637   ; 1.00   
	; *** this is the distance betwee TRP CA in the starting structre
	; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
	; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.


pull_group3_name        = ACT2
pull_group4_name        = CAT2
pull_coord2_geometry            = distance      ; simple distance increase
pull_coord2_groups      = 3 4
pull_coord2_dim         = Y Y Y         ; all x,y,z components possible
pull_coord2_rate        = 0.10          ; 0.01 nm per ps = 10 nm per ns
pull_coord2_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord2_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord2-init        = 3.678   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.

pull_group5_name        = ACT3
pull_group6_name        = CAT3
pull_coord3_geometry            = distance      ; simple distance increase
pull_coord3_groups      = 5 6
pull_coord3_dim         = Y Y Y         ; all x,y,z components possible
pull_coord3_rate        = 0.10          ; 0.01 nm per ps = 10 nm per ns
pull_coord3_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord3_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord3-init        = 3.662   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.


pull_group7_name        = ACT4
pull_group8_name        = CAT4
pull_coord4_geometry            = distance      ; simple distance increase
pull_coord4_groups      = 7 8
pull_coord4_dim         = Y Y Y         ; all x,y,z components possible
pull_coord4_rate        = 0.10          ; 0.01 nm per ps = 10 nm per ns
pull_coord4_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord4_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord4-init        = 3.726   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.


pull_group9_name        = CAT1
pull_group10_name        = CAT2
pull_coord5_geometry            = distance      ; simple distance increase
pull_coord5_groups      = 9 10
pull_coord5_dim         = Y Y Y         ; all x,y,z components possible
pull_coord5_rate        = 0.00          ; 0.01 nm per ps = 10 nm per ns
pull_coord5_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord5_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord5-init        = 4.605   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.

pull_group11_name        = CAT1
pull_group12_name        = CAT3
pull_coord6_geometry            = distance      ; simple distance increase
pull_coord6_groups      = 11 12
pull_coord6_dim         = Y Y Y         ; all x,y,z components possible
pull_coord6_rate        = 0.00          ; 0.01 nm per ps = 10 nm per ns
pull_coord6_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord6_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord6-init        = 5.271   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.

pull_group13_name        = CAT2
pull_group14_name        = CAT4
pull_coord7_geometry            = distance      ; simple distance increase
pull_coord7_groups      = 13 14
pull_coord7_dim         = Y Y Y         ; all x,y,z components possible
pull_coord7_rate        = 0.00          ; 0.01 nm per ps = 10 nm per ns
pull_coord7_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord7_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord7-init        = 5.385   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.


pull_group15_name        = CAT3
pull_group16_name        = CAT4
pull_coord8_geometry            = distance      ; simple distance increase
pull_coord8_groups      = 15 16
pull_coord8_dim         = Y Y Y         ; all x,y,z components possible
pull_coord8_rate        = 0.00          ; 0.01 nm per ps = 10 nm per ns
pull_coord8_k           = 50.0           ; kJ mol^-1 nm^-2
pull_coord8_start              = no            ; yes           ; define initial COM distance > 0,
                                        ;  i.e. if yes, add the COM distance of the starting conformation to pull-coord1-init
pull-coord8-init        = 4.473   ; 1.00   
        ; *** this is the distance betwee TRP CA in the starting structre
        ; the initial COM distance is the reference distance for the first frame. This is useful because if we are attempting
        ; to pull 5.0 nm, converting the initial COM distance to zero (i.e., pull_start = no) makes this interpretation difficult.


pull-nstxout	        = 5000 	; (50) frequency for writing out the COMs of all the pull group (0 is never)
pull-nstfout	        = 5000 	; (50) frequency for writing out the force of all the pulled group (0 is never)

; no FEP gmx5.0.6 !!!
free-energy 		= no
"""

    mdpfile = 'mdp/pull_r%.2f_gmx5.1.2.mdp'%r
    fout = open(mdpfile, 'w')
    fout.write(mdp_text)
    fout.close()
    print 'Wrote:', mdpfile



####################################
# Next, write the batch script 
for r in range(10):
	outfile = 'RUN%d/qsub_%d.sh'%(r,r)

	outtxt = """#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -N pull_test_200
#PBS -q normal 
#PBS -l nodes=1:ppn=20
#PBS -o pull_test_200 
#PBS 

cd $PBS_O_WORKDIR
module load gromacs/5.1.2
"""


    	mdpfile = '../mdp/pull_r%3.2f_gmx5.1.2.mdp'%r
    	outtxt += "gmx grompp -f %s -c solvent_ions_equilibrated2.gro -p CHC1_dry_GMX.top -n index.ndx -o pull%d.tpr\n"%(mdpfile,r)
    	outtxt += "gmx mdrun -nt 20 -s pull%d.tpr -c solvent_ions_equilibrated2.gro\n"%(r)

	fout = open(outfile, 'w')
	fout.write(outtxt)
	fout.close()
	print 'Wrote', outfile


######## NOTES on mdpfile options #########
"""
Options to specify input and output files:

 -s     [<.tpr/.tpb/...>] (topol.tpr) (Input) Run input file: tpr tpb tpa
 -o     [<.trr/.cpt/...>] (traj.trr) (Output)
     Full precision trajectory: trr cpt trj tng
 -x     [<.xtc/.tng>] (traj_comp.xtc) (Output, Opt.)
     Compressed trajectory (tng format or portable xdr format)
 -cpi   [<.cpt>] (state.cpt) (Input, Opt.) Checkpoint file
 -cpo   [<.cpt>] (state.cpt) (Output, Opt.) Checkpoint file
 -c     [<.gro/.g96/...>] (confout.gro) (Output)
     Structure file: gro g96 pdb brk ent esp
 -e     [<.edr>] (ener.edr) (Output) Energy file
 -g     [<.log>] (md.log) (Output) Log file
 -dhdl  [<.xvg>] (dhdl.xvg) (Output, Opt.) xvgr/xmgr file
 -field [<.xvg>] (field.xvg) (Output, Opt.) xvgr/xmgr file
 -table [<.xvg>] (table.xvg) (Input, Opt.) xvgr/xmgr file
 -tabletf [<.xvg>] (tabletf.xvg) (Input, Opt.) xvgr/xmgr file
 -tablep [<.xvg>] (tablep.xvg) (Input, Opt.) xvgr/xmgr file
 -tableb [<.xvg>] (table.xvg) (Input, Opt.) xvgr/xmgr file
 -rerun [<.xtc/.trr/...>] (rerun.xtc) (Input, Opt.)
     Trajectory: xtc trr cpt trj gro g96 pdb tng
 -tpi   [<.xvg>] (tpi.xvg) (Output, Opt.) xvgr/xmgr file
 -tpid  [<.xvg>] (tpidist.xvg) (Output, Opt.) xvgr/xmgr file
 -ei    [<.edi>] (sam.edi) (Input, Opt.) ED sampling input
 -eo    [<.xvg>] (edsam.xvg) (Output, Opt.) xvgr/xmgr file
 -devout [<.xvg>] (deviatie.xvg) (Output, Opt.) xvgr/xmgr file
 -runav [<.xvg>] (runaver.xvg) (Output, Opt.) xvgr/xmgr file
 -px    [<.xvg>] (pullx.xvg) (Output, Opt.) xvgr/xmgr file
 -pf    [<.xvg>] (pullf.xvg) (Output, Opt.) xvgr/xmgr file
 -ro    [<.xvg>] (rotation.xvg) (Output, Opt.) xvgr/xmgr file
 -ra    [<.log>] (rotangles.log) (Output, Opt.) Log file
 -rs    [<.log>] (rotslabs.log) (Output, Opt.) Log file
 -rt    [<.log>] (rottorque.log) (Output, Opt.) Log file
 -mtx   [<.mtx>] (nm.mtx) (Output, Opt.) Hessian matrix
 -dn    [<.ndx>] (dipole.ndx) (Output, Opt.) Index file
 -multidir [<dir> [...]] (rundir) (Input, Opt.) Run directory
 -membed [<.dat>] (membed.dat) (Input, Opt.) Generic data file
 -mp    [<.top>] (membed.top) (Input, Opt.) Topology file
 -mn    [<.ndx>] (membed.ndx) (Input, Opt.) Index file
 -if    [<.xvg>] (imdforces.xvg) (Output, Opt.) xvgr/xmgr file
 -swap  [<.xvg>] (swapions.xvg) (Output, Opt.) xvgr/xmgr file

"""

