# AdvLigPrep
A semi-automated parm7 preparation script for AMBER TI.
This script can also make parmed input that changes the parameters of a residue to the ones from another force field.

IMPORTANT: When using AdvLigPrep for conducting TI, users are expected to have solid knowledge about AMBER TI, especially the linear scaling/single topology approach.
      The generated parmed scripts are not meant to be directly used and need proper edits before use. 
     
To Use:
1. Build two separate parm7 files for the ligands. Ligand B need to be a substructure of ligand A (unless you know what you are doing). 
   For single mutation, build 2 stand-alone amino acids using "sequence" in tleap. 
2. Create a mapping file indicating which atoms are paired.
   Only include pairing atom with different atom name in the mapping file. See the example for Ile to Val mutation.
   Atoms with same atom name will be paired by default, so please change the atom names of the atoms that are not supposed to be paired.
3. Use the following command to generate the output files.

   exec.py "A.parm7" "B.parm7" "map" "prm.sh"
   
   A.parm7 and B.parm7 are the parm7 files for the ligands.
   map is the mapping file.
   prm.sh is the output file.
4. Please read prm.sh carefully and be sure that you know what each line is doing.
   Edit prm.sh if needed. 
   parmed commands in prm.sh will change the parameters of A to to the parameters of B. 
5. To use prm.sh for setting up parm7/rst7 for AMBER TI.
   Follow the amber manual. Before timerge source prm.sh to change the parameter of the 2nd copy of A.
   Do not use softcore when using AdvLigPrep (unless you know what you are doing). 

Note:
1. For amino acids like A, P and G which have different backbone dihedral angles involving atoms from neighboring residues. Manual edit the atom selection masks in prm.sh so they point to the neighboring residues.

Credits to:
Junjie Zou
