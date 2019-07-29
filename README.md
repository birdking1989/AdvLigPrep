# AdvLigPrep
A semi-automated parm7 preparation script for AMBER TI.
Note: Users are required to have solid knowledge of AMBER TI, especially the linear scaling/single topology approach.
      Output files are not meant to be directly used and need proper edits before use. 
     
To Use:
1. Build two separate parm7 files for the ligands. Ligand B need to be a substructure of ligand A (unless you know what you are doing). 
   For single mutation, build 2 standalone amino acids using "sequence" in tleap. 
2. Create a mapping file indicating which atoms are paired.
   Include pairing atom with different atom name in the mapping file. See the example for Ile to Val mutation.
   Atoms with same atom name will be paired, so please change the atom names of the atoms if you do not want to pair them.
3. Use the following command to generate the output files.
   exec.py "A.parm7" "B.parm7" "map" "prm.sh"
   A.parm7 and B.parm7 are the parm7 files for the ligands.
   map is the mapping file.
   prm.sh is the output file.
4. Edit prm.sh if needed.
   parmed commands in prm.sh will change the parameters of A to to the parameters of B. 
5. To use prm.sh in AMBER TI.
   Follow the amber manual. Before timerge source prm.sh to change the parameter of the 2nd copy of A.
