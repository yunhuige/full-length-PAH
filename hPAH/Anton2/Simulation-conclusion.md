### APAH_prod
2023920 ps

Putative activated state full length hPAH (ACT domain dimer: c1-c2, c3-c4). This simulation aims to test stability of this conformation and sample possible motions.

### RS_PAH
2263680 ps

Resting state full length hPAH (constructed based on PDBid 6n1k). This simulation aims to sample motions of resting state conformation.

### t4_prod
1122240 ps

Similar to RS_PAH. Aiming for different sampling from RS_PAH.

### t23_prod
1122240 ps

Similar to RS_PAH. Aiming for different sampling from RS_PAH.

### UMB1_prod
1282560 ps

Starting from a snapshot in umbrella simulations which pull ACT domain out of the original position. This simulation aims to test if dimerization could happen when ACT domains are far from the original pocket in the resting state. The ACT domains are maintain folded conformation during the umbrella simulations.

### UMB8_prod
1362720 ps

Similar to UMB1 but from another umbrella simulations. Hopefully could sample more conformational space/motions besides UMB1.

### UMB20_prod
1282560 ps

Similar to UMB1 and UMB8, but two ACT domains are close to each other. This simulation aims to sample motions during dimerization.

### alter_prod
561120 ps

Alternative putative activated state full legnth hPAH (ACT domain dimer: c1-c3, c2-c4). This structure is constrcuted using a series of umbrellas in OpenMM simulations. Multiple trials were performed and this is the only one that worked.


total: 11181360 ps = 11 us
This total time does not include test runs and equilibration runs.

