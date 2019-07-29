#!/usr/bin/python3
import sys
import parmed as pmd


# toppar1 = sys.argv[1]
# toppar2 = sys.argv[2]
# mapfile = sys.argv[3]
#
# parm1 = pmd.load_file(toppar1)
# parm2 = pmd.load_file(toppar2)
#
# f = open('prm.sh', 'w')
# f.close()


def wrtchrg(changelst, file):
    """
    append the change charge section
    :param changelst: pair list from chrgpair function
    :param file: file to append to
    :return:
    """
    f = open(file, 'a')
    f.write("# number of charges to change: %4d" % (len(changelst)) + "\n")
    delchrg = 0
    for i in changelst:
        atmname = i[0].name
        chrg = i[1].charge
        f.write("change charge :2@%s %.4f" % (atmname, chrg) + "\n")
        delchrg = delchrg + i[1].charge - i[0].charge

    f.write("# net charge change: %.4f" % delchrg + "\n")
    f.close()
    return


def rmvchrg(changelst, file):
    """
    remove upaired charges on mol1
    :param changelst: unpaired list of mol1
    :param file: file to append to
    :return:
    """
    f = open(file, 'a')
    f.write("# number of unpiared charges to remove: %4d" % (len(changelst)) + "\n")
    delchrg = 0
    for i in changelst:
        atmname = i.name
        f.write("change charge :2@%s 0.0" % atmname + "\n")
        delchrg = delchrg - i.charge

    f.write("# net charge change: %.4f" % delchrg + "\n")
    f.close()
    return


def wrtlj(changelst, file):
    f = open(file, 'a')
    f.write("# number of LJs to change: %4d" % (len(changelst)) + "\n")
    for i in changelst:
        atmname = i[0].name
        eps = i[1].atom_type.epsilon
        rmin = i[1].atom_type.rmin
        eps14 = i[1].atom_type.epsilon_14
        rmin14 = i[1].atom_type.rmin_14

        f.write("addLJType :2@%s radius %.4f epsilon %.4f radius_14 %.4f epsilon_14 %.4f"
                   % (atmname, rmin, eps, rmin14, eps14) + "\n")
    f.close()
    return


def rmvlj(changelst, file):
    f = open(file, 'a')
    f.write("# number of LJs to remove: %4d" % (len(changelst)) + "\n")
    for i in changelst:
        atmname = i.name
        f.write("addLJType :2@%s radius 0.0 epsilon 0.0 radius_14 0.0 epsilon_14 0.0"
                   % atmname + "\n")
    f.close()
    return


def wrtbond(changelst, file):
    f = open(file, 'a')
    f.write("# number of bonds to change: %4d" % (len(changelst)) + "\n")
    for i in changelst:
        atmname1 = i[0].atom1.name
        atmname2 = i[0].atom2.name
        k = i[1].type.k
        req = i[1].type.req

        f.write("setBond :2@%s :2@%s %.4f %.4f"
                   % (atmname1, atmname2, k, req) + "\n")
    f.close()
    return


def wrtang(changelst, file):
    f = open(file, 'a')
    f.write("# number of angles to change: %4d" % (len(changelst)) + "\n")
    for i in changelst:
        atmname1 = i[0].atom1.name
        atmname2 = i[0].atom2.name
        atmname3 = i[0].atom3.name
        k = i[1].type.k
        theteq = i[1].type.theteq

        f.write("setAngle :2@%s :2@%s :2@%s %.4f %.4f"
                   % (atmname1, atmname2, atmname3, k, theteq) + "\n")
    f.close()
    return


def wrtdihe(changelst, file):
    f = open(file, 'a')
    f.write("# number of dihedrals to change: %4d" % (len(changelst)) + "\n")
    for i in changelst:
        atmname1 = i[0].atmlst[0].name
        atmname2 = i[0].atmlst[1].name
        atmname3 = i[0].atmlst[2].name
        atmname4 = i[0].atmlst[3].name
        f.write("deleteDihedral :2@%s :2@%s :2@%s :2@%s"
                   % (atmname1, atmname2, atmname3, atmname4) + "\n")

    for i in changelst:
        if i[0].imp:
            typestr = 'type improper'
        else:
            typestr = ''

        atmname1 = i[0].atmlst[0].name
        atmname2 = i[0].atmlst[1].name
        atmname3 = i[0].atmlst[2].name
        atmname4 = i[0].atmlst[3].name

        for j in i[1].diheset:
            f.write("addDihedral :2@%s :2@%s :2@%s :2@%s %.4f %.4f %.4f %s"
                       % (atmname1, atmname2, atmname3, atmname4,
                          j.phi_k, j.per, j.phase, typestr) + "\n")
    f.close()
    return

