#!/usr/bin/python3
import sys
import parmed as pmd
import prmgen as prm
import prntprm as prnt

toppar1 = sys.argv[1]
toppar2 = sys.argv[2]
mapfile = sys.argv[3]
filename = sys.argv[4]

parm1 = pmd.load_file(toppar1)
parm2 = pmd.load_file(toppar2)

f = open(filename, 'w')
f.close()

pair = prm.atompairfromfile(parm1, parm2, mapfile)
matchlst, unplst1, unplst2 = prm.getatomlist(parm1, parm2, pair)
totpair = matchlst + pair + [[i, ''] for i in unplst1] + [['', i] for i in unplst1]


prm.printlst(pair, matchlst, unplst1, unplst2)

# change charge
chrglst = prm.chrgpair(parm1, parm2, matchlst + pair)
prnt.wrtchrg(chrglst, filename)
prnt.rmvchrg(unplst1, filename)

# addLJType
ljlst = prm.LJpair(parm1, parm2, matchlst + pair)
prnt.wrtlj(ljlst, filename)
prnt.rmvlj(unplst1, filename)

# setBond
bondlst, l1, l2 = prm.bondpair(parm1, parm2, totpair)
prnt.wrtbond(bondlst, filename)

# setAngle
anglelst, l1, l2 = prm.anglepair(parm1, parm2, totpair)
prnt.wrtang(anglelst, filename)

# deleteDihedrals and addDihedrals
dihelst, l1, l2, g1, g2 = prm.dihedralpair(parm1, parm2, totpair)
prnt.wrtdihe(dihelst, filename)
