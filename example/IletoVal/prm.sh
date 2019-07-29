# number of charges to change:   12
change charge :2@CA -0.0875
change charge :2@HA 0.0969
change charge :2@CB 0.2985
change charge :2@HB -0.0297
change charge :2@CG2 -0.3192
change charge :2@HG21 0.0791
change charge :2@HG22 0.0791
change charge :2@HG23 0.0791
change charge :2@CG1 -0.3192
change charge :2@HG12 0.0791
change charge :2@HG13 0.0791
change charge :2@CD1 0.0791
# net charge change: 0.0558
# number of unpiared charges to remove:    3
change charge :2@HD11 0.0
change charge :2@HD12 0.0
change charge :2@HD13 0.0
# net charge change: -0.0558
# number of LJs to change:    1
addLJType :2@CD1 radius 1.4870 epsilon 0.0157 radius_14 1.4870 epsilon_14 0.0157
# number of LJs to remove:    3
addLJType :2@HD11 radius 0.0 epsilon 0.0 radius_14 0.0 epsilon_14 0.0
addLJType :2@HD12 radius 0.0 epsilon 0.0 radius_14 0.0 epsilon_14 0.0
addLJType :2@HD13 radius 0.0 epsilon 0.0 radius_14 0.0 epsilon_14 0.0
# number of bonds to change:    1
setBond :2@CG1 :2@CD1 340.0000 1.0900
# number of angles to change:    3
setAngle :2@CB :2@CG1 :2@CD1 50.0000 109.5000
setAngle :2@HG13 :2@CG1 :2@CD1 35.0000 109.5000
setAngle :2@HG12 :2@CG1 :2@CD1 35.0000 109.5000
# number of dihedrals to change:    5
deleteDihedral :2@CG1 :2@CB :2@CA :2@C
deleteDihedral :2@CG2 :2@CB :2@CG1 :2@CD1
deleteDihedral :2@CA :2@CB :2@CG1 :2@CD1
deleteDihedral :2@N :2@CA :2@CB :2@CG1
deleteDihedral :2@HB :2@CB :2@CG1 :2@CD1
addDihedral :2@CG1 :2@CB :2@CA :2@C 0.1120 4.0000 0.0000 
addDihedral :2@CG1 :2@CB :2@CA :2@C 0.4060 1.0000 180.0001 
addDihedral :2@CG1 :2@CB :2@CA :2@C 0.1480 3.0000 0.0000 
addDihedral :2@CG1 :2@CB :2@CA :2@C 0.2890 2.0000 180.0001 
addDihedral :2@CG2 :2@CB :2@CG1 :2@CD1 0.1600 3.0000 0.0000 
addDihedral :2@CA :2@CB :2@CG1 :2@CD1 0.1600 3.0000 0.0000 
addDihedral :2@N :2@CA :2@CB :2@CG1 0.0010 4.0000 180.0001 
addDihedral :2@N :2@CA :2@CB :2@CG1 0.3370 1.0000 0.0000 
addDihedral :2@N :2@CA :2@CB :2@CG1 0.1480 3.0000 0.0000 
addDihedral :2@N :2@CA :2@CB :2@CG1 0.2160 2.0000 180.0001 
addDihedral :2@HB :2@CB :2@CG1 :2@CD1 0.1500 3.0000 0.0000 
