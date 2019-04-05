Email from Marcela about how to get dihedral angles parameters for Anton format from Amber FF.
```
hi Yunhui,

You may want to try the Intermol conversion, in my test it gave dihedral angles.
It is just that some aspects of the FF are incomplete, that is why you need to run viparr after Intermol.
If Intermol gives you dihedral angles make sure they are still there when running viparr afterwards.

Alternatively, this is how I converted one of the angles, I am sending the instructions so that you can continue and check.

on kollman.psc.edu we have AmberTools and that is what I used. Since this are Amber FF I went through Amber. 

module load  AmberTools18

you will want to run tleap with frcmod.ff99SBildn and the modified frcmod and look at the differences in the created files.

tleap
>source ./Runtleap1

here Runtleap1 is:

source  /usr/local/packages/AmberTools18/dat/leap/cmd/oldff/leaprc.ff99SBildn
loadamberparams frcmod.ff99SBildn
m=loadpdb pdbfile
saveamberparm m prmtop1 inpcrd1

Do the same of the other frcmod

You will get the parameter and starting structures prmtop and inpcrd. 
Then on Anton follow the instructions to convert Amber to dms:

viparr-convert-prmtop.py -c <rst file>  -o system.dms <prmtop file>

and 
dms-dump system.dms >system.txt

Repeat for the other dms and you should have two txt files with the dihedrals in Anton format.
It is best to use a small pdb file and do the angles one at a time.

As with any script we provide we advise that the scientist (you) test for correctness,
I have not looked at the definition of dihedral angles so I cannot assess as to whether the numbers are correct or not.
Check against the definitions of dihedral angles for Desmond.
Hope this helps, let me know any problems. Marcela
```

Correspondingly, I followed these suggestions and finally got these parameters updated for ff99sb-ildn-nmr from ff99sb-ildn:

   {"type": ["N", "CT", "C", "N"], "params": {"phi0": 0.0, "fc0": 2.73, "fc1": -0.64, "fc2": -1.21, "fc3": -0.75, "fc4": 0.13, "fc5": 0.0, "fc6": 0.0}, "memo": " phases for psi four amplitudes and, updated for ffsb-ildn-nmr"},
   {"type": ["C", "N", "CT", "C"], "params": {"phi0": 0.0, "fc0": 1.04, "fc1": 0.0, "fc2": 0.11, "fc3": 0.52, "fc4": 0.41, "fc5": 0.0, "fc6": 0.0}, "memo": " phases for phi four amplitudes and, updated for ffsb-ildn-nmr"},
   {"type": ["CT", "CT", "N", "C"], "params": {"phi0": 0.0, "fc0": 4.51, "fc1": 2.43, "fc2": 1.63, "fc3": 0.13, "fc4": 0.32, "fc5": 0.0, "fc6": 0.0}, "memo": " phases for phi' four amplitudes and, updated for ffsb-ildn-nmr"},
   {"type": ["CT", "CT", "C", "N"], "params": {"phi0": 0.0, "fc0": 1.67, "fc1": -0.41, "fc2": 0.31, "fc3": 0.70, "fc4": 0.25, "fc5": 0.0, "fc6": 0.0}, "memo": " phases for psi' four amplitudes and, updated for ffsb-ildn-nmr"},
