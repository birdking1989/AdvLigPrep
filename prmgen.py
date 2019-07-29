# toppar1 = sys.argv[1]
# toppar2 = sys.argv[2]
# mapfile = sys.argv[3]
#
# parm1 = pmd.load_file(toppar1)
# parm2 = pmd.load_file(toppar2)

def atompairfromfile(parm1, parm2, mapfile):
    """
    This function reads in a mapfile which contains the changing atom pairs
    with different atom name. Then a pair list of atoms in the format of
    parmed atoms is returned

    Parameters
    ----------
    parm1,parm2: parm7 file of molecules
    mapfile: atom names of changing atoms in pair

    Returns
    -------
    A 2D list of pairs defined in mapfile in the format of parmed atoms
    """
    atmpair = []
    with open(mapfile) as f:
        for line in f:
            atmpairinfile = line.split()
            findpair=False
            for atm1, atm2 in ((a1, a2) for a1 in parm1.atoms for a2 in parm2.atoms):
                if atm1.name==atmpairinfile[0] and atm2.name==atmpairinfile[1]:
                    atmpair.append([atm1, atm2])
                    findpair=True
                    break
            if findpair:
                break
    return atmpair


def getatomlist(parm1, parm2, changingpair):
    """
    This function construct a list of atom pairs with same atom name in both
    molecules and a list of atoms with no matching.

    Parameters
    ----------
    parm1,parm2: parm7 file of molecules
    changingpair: list of changing atom pair with different atom names
    Returns
    -------
    A list of matched pair and a list of atoms with no match
    """
    matchpairlst = []
    nomatchlst1 = []
    nomatchlst2 = []
    for atm1, atm2 in ((a1, a2) for a1 in parm1.atoms for a2 in parm2.atoms):
        if atm1.name == atm2.name:
            matchpairlst.append([atm1, atm2])


    for atm1 in parm1.atoms:
        findpair = False
        for atm2 in parm2.atoms:
            if atm1.name == atm2.name:
                findpair = True
                break
            for sublist in changingpair:
                if atm1 is sublist[0]:
                    findpair = True
                    break
        if not findpair:
            nomatchlst1.append(atm1)


    for atm2 in parm2.atoms:
        findpair = False
        for atm1 in parm1.atoms:
            if atm2.name == atm1.name:
                findpair = True
                break
            for sublist in changingpair:
                if atm2 is sublist[1]:
                    findpair = True
                    break
        if not findpair:
            nomatchlst2.append(atm2)

    return matchpairlst, nomatchlst1, nomatchlst2


def printlst(pair, matchedpair, lst1, lst2):
    """
    This function prints atom names regarding TI

    :param pair: pair2 defined by user
    :param matchedpair: pair2 with same atom name in mol1 and mol2
    :param lst1: unpaired atoms in mol1
    :param lst2: unpaired atoms in mol2
    :return: print on screen
    """
    matchname = []
    for i in matchedpair:
        matchname.append(i[0].name)

    matchmask = ','.join(matchname)

    pairname1 = []
    pairname2 = []
    for i in pair:
        pairname1.append(i[0].name)
        pairname2.append(i[1].name)

    pairmask1 = ','.join(pairname1)
    pairmask2 = ','.join(pairname2)

    unpairedname1 = []
    for i in lst1:
        unpairedname1.append(i.name)

    unpairedmask1 = ','.join(unpairedname1)

    unpairedname2 = []
    for i in lst2:
        unpairedname2.append(i.name)

    unpairedmask2 = ','.join(unpairedname2)

    timask1 = ','.join(pairname1 + unpairedname1)
    timask2 = ','.join(pairname2 + unpairedname2)

    print("number of atoms with same atom name:", len(matchmask))
    print(matchmask)
    print("pairing defined by user:")
    for itm in pair:
        print(itm[0].name, "--", itm[1].name)

    print("atoms unpaired in mol1: @", unpairedmask1)
    print("atoms unpaired in mol2: @", unpairedmask2)

    print("R1: @",timask1)
    print("R2: @",timask2)
    return


# pair = atompairfromfile(parm1, parm2, mapfile)
# matchlst, unplst1, unplst2 = getatomlist(parm1, parm2, pair)
# totpair = matchlst + pair + [[i, ''] for i in unplst1] + [['', i] for i in unplst1]
#
#
# printlst(pair, matchlst, unplst1, unplst2)


def bondpair(parm1, parm2, pairlist):         #todo bond
    """
    Find bonds that have different k and req in two parm file and bonds unpaired in mol1&2
    :param parm1: parm file of mol1
    :param parm2: parm file of mol2
    :param pairlist: 2d list of parm.atoms
    :return: changelst: setBond list
             remlist1: unparied bonds in mol1
             bondlist2: unpaired bonds in mol2
    """
    atmlist1, atmlist2 = [i[0] for i in pairlist], [i[1] for i in pairlist]
    bondlist1 = [i for i in parm1.bonds]
    bondlist2 = [i for i in parm2.bonds]
    remlist1 = [i for i in parm1.bonds]
    changelst = []
    for i in bondlist1:
        for j in bondlist2:
            fwd = atmlist2[atmlist1.index(i.atom1)] == j.atom1 and atmlist2[atmlist1.index(i.atom2)] == j.atom2
            rev = atmlist2[atmlist1.index(i.atom1)] == j.atom2 and atmlist2[atmlist1.index(i.atom2)] == j.atom1
            if fwd or rev:
                remlist1.remove(i)
                bondlist2.remove(j)
                if i.type == j.type:
                    break
                else:
                    changelst.append([i, j])
                    break

    return changelst, remlist1, bondlist2


# cl, l1, l2 = bondpair(parm1, parm2, totpair)

def anglepair(parm1, parm2, pairlist):          # todo angle
    """
    Find bonds that have different k and thetaeq in two parm file and angles unpaired in mol1&2
    :param parm1: parm file of mol1
    :param parm2: parm file of mol2
    :param pairlist: 2d list of parm.atoms
    :return: changelst: setAngle list
             remlist1: unparied angles in mol1
             anglelist2: unpaired angles in mol2
    """
    atmlist1, atmlist2 = [i[0] for i in pairlist], [i[1] for i in pairlist]
    anglelist1 = [i for i in parm1.angles]
    anglelist2 = [i for i in parm2.angles]
    remlist1 = [i for i in parm1.angles]
    changelst = []
    for i in anglelist1:
        for j in anglelist2:
            fwd = atmlist2[atmlist1.index(i.atom1)] == j.atom1 and atmlist2[atmlist1.index(i.atom3)] == j.atom3 \
                and atmlist2[atmlist1.index(i.atom2)] == j.atom2
            rev = atmlist2[atmlist1.index(i.atom1)] == j.atom3 and atmlist2[atmlist1.index(i.atom3)] == j.atom1 \
                and atmlist2[atmlist1.index(i.atom2)] == j.atom2
            if fwd or rev:
                remlist1.remove(i)
                anglelist2.remove(j)
                if i.type == j.type:
                    break
                else:
                    changelst.append([i, j])
                    break

    return changelst, remlist1, anglelist2


# cl, l1, l2 = anglepair(parm1, parm2, totpair)
# print(len(cl),cl)
# print(len(l1),l1)
# print(len(l2),l2)
# todo dihe
def LJpair(parm1, parm2, pairlist):       # todo LJ
    """
    Find atoms that have different LJ parameters and atoms that need to remove LJ interactions.
    :param parm1: parm file of mol1
    :param parm2: parm file of mol2
    :param pairlist: 2d list of paired atoms. Note: not including unpaired
    :return: changelst: addLJtype list
    """
    changelst = []
    for i in pairlist:
        if not (i[0].atom_type.epsilon == i[1].atom_type.epsilon and i[0].atom_type.rmin == i[1].atom_type.rmin):
            changelst.append(i)

    return changelst


# cl = LJpair(parm1, parm2, matchlst + pair)
# print([[i[0].atom_type.epsilon,i[1].atom_type.epsilon] for i in cl])

def chrgpair(parm1, parm2, pairlist):       # todo charge
    """
    Find atoms that have different partial charges and atoms that need to change partial charges.
    :param parm1: parm file of mol1
    :param parm2: parm file of mol2
    :param pairlist: 2d list of paired atoms. Note: not including unpaired
    :return: changelst: change charge list
    """
    changelst = []
    for i in pairlist:
        if not (i[0].charge == i[1].charge):
            changelst.append(i)

    return changelst


class Groupeddihedrals:
    """
    This class is specifically for comparing dihedrals with multiplicity.
    """
    def __init__(self, atmlst, diheset, imp):
        """
        :param atmlst: a list of atoms involved in dihedral
        :param diheset: a set of dihedral types associated with atmlst
        :param imp: true or false of being a improper dihedral
        """
        self.atmlst = atmlst
        self.diheset = diheset
        self.imp = imp

    def same_dihe(self,other):
        """
        True if dihedral.type sets match and dihedral.improper match
        :param other:
        :return: true or false
        """
        return self.diheset == other.diheset and self.imp == other.imp

def dihedralpair(parm1, parm2, pairlist):
    """
    Find dihedrals that have different parameters in mol1 and mol2.
    :param parm1: parm file of mol1
    :param parm2: parm file of mol2
    :param pairlist: 2d list of paired atoms.
    :return: changelst: deleteDihedrals and addDihedrals list
             remlist1: unpaired grouped dihedrals in mol1
             remlist2: unpaired grouped dihedrals in mol2
             grplist1: all grouped dihedrals in mol1
             grplist2: all grouped dihedrals in mol2
    """
    atmlist1, atmlist2 = [i[0] for i in pairlist], [i[1] for i in pairlist]
    dihelist1 = [i for i in parm1.dihedrals]
    dihelist2 = [i for i in parm2.dihedrals]
    grplst1 = []
    grplst2 = []
    changelst = []

    # group dihedral terms with same atm1, atm2, atm3 and atm4 construct a list of GroupedDihedral
    while dihelist1:
        diheset=set()
        atmlst = [dihelist1[0].atom1, dihelist1[0].atom2,
                  dihelist1[0].atom3, dihelist1[0].atom4]
        deletelst = []
        for idx, i in enumerate(dihelist1):
            if dihelist1[0].improper == i.improper and \
                ((dihelist1[0].atom1 == i.atom1 and dihelist1[0].atom2 == i.atom2 and
                 dihelist1[0].atom3 == i.atom3 and dihelist1[0].atom4 == i.atom4) or
                 (dihelist1[0].atom4 == i.atom1 and dihelist1[0].atom3 == i.atom2 and
                  dihelist1[0].atom2 == i.atom3 and dihelist1[0].atom1 == i.atom4)):
                diheset.add(i.type)
                deletelst.append(idx)

        grplst1.append(Groupeddihedrals(atmlst, diheset, dihelist1[0].improper))
        deletelst.sort()
        while deletelst:
            delidx = deletelst.pop()
            del dihelist1[delidx]

    while dihelist2:
        diheset=set()
        atmlst = [dihelist2[0].atom1, dihelist2[0].atom2,
                  dihelist2[0].atom3, dihelist2[0].atom4]
        deletelst=[]
        for idx, i in enumerate(dihelist2):
            if dihelist2[0].improper == i.improper and \
                ((dihelist2[0].atom1 == i.atom1 and dihelist2[0].atom2 == i.atom2 and
                 dihelist2[0].atom3 == i.atom3 and dihelist2[0].atom4 == i.atom4) or
                 (dihelist2[0].atom4 == i.atom1 and dihelist2[0].atom3 == i.atom2 and
                  dihelist2[0].atom2 == i.atom3 and dihelist2[0].atom1 == i.atom4)):
                diheset.add(i.type)
                deletelst.append(idx)

        grplst2.append(Groupeddihedrals(atmlst, diheset, dihelist2[0].improper))
        deletelst.sort()
        while deletelst:
            delidx = deletelst.pop()
            del dihelist2[delidx]

    remlist1 = grplst1.copy()
    remlist2 = grplst2.copy()

    # loop over to search matched pairs
    for i in grplst1:
        for j in grplst2:
            fwd = (atmlist2[atmlist1.index(i.atmlst[0])] == j.atmlst[0] and
                   atmlist2[atmlist1.index(i.atmlst[1])] == j.atmlst[1] and
                   atmlist2[atmlist1.index(i.atmlst[2])] == j.atmlst[2] and
                   atmlist2[atmlist1.index(i.atmlst[3])] == j.atmlst[3])
            rev = (atmlist2[atmlist1.index(i.atmlst[3])] == j.atmlst[0] and
                   atmlist2[atmlist1.index(i.atmlst[2])] == j.atmlst[1] and
                   atmlist2[atmlist1.index(i.atmlst[1])] == j.atmlst[2] and
                   atmlist2[atmlist1.index(i.atmlst[0])] == j.atmlst[3])
            # boolean for being the same normal dihedral
            ifdihematch = (fwd or rev) and (not i.imp)

            impseq = (atmlist2[atmlist1.index(i.atmlst[0])] == j.atmlst[0] and
                      {atmlist2[atmlist1.index(i.atmlst[1])], atmlist2[atmlist1.index(i.atmlst[2])],
                       atmlist2[atmlist1.index(i.atmlst[3])]} == {j.atmlst[1], j.atmlst[2], j.atmlst[3]})
            # boolean for being the same improper dihedral
            ifimpmatch = impseq and i.imp

            if ifdihematch or ifimpmatch:
                remlist1.remove(i)
                remlist2.remove(j)
                if i.diheset == j.diheset:
                    break
                else:
                    changelst.append([i, j])
                    break

    return changelst, remlist1, remlist2, grplst1, grplst2


# cl, l1, l2, g1, g2 = dihedralpair(parm1, parm2, totpair)
# print(len(cl),cl)
# print(len(l1),l1)
# print(len(l2),l2)

def rmv23dihe(grpdihelst, diheatms):
    """
    this function finds dihedrals with the same atm2,3 as the diheatms in a groupedDihedral list.
    Not including the input dihedral
    :param grpdihelst: groupedDihedral list
    :param diheatms: list of atoms involved in the dihedral to match
    :return: dellst: a list of group dihedral to be deleted to remove redundant constraints
    """
    dellst=[]
    for j in grpdihelst:
        fwd = (diheatms[1] == j.atmlst[1] and diheatms[2] == j.atmlst[2]) and \
              (diheatms[0] != j.atmlst[0] or diheatms[3] != j.atmlst[3])
        rev = (diheatms[2] == j.atmlst[1] and diheatms[1] == j.atmlst[2]) and \
              (diheatms[3] != j.atmlst[0] or diheatms[0] != j.atmlst[3])
        # boolean for having same atm2, atm3 and is not an improper dihedral
        ifdihematch = (fwd or rev) and (not j.imp)
        if ifdihematch:
            dellst.append(j)

    return dellst

