
def liste_colone():
    liste = []
    i = 0
    while i < 7:
        liste.append(str(i))
        liste.append("|")
        i += 1
    liste.append("\n")
    return liste


def liste_moins():
    liste = []
    i = 0
    while i < 14:
        liste.append("-")
        i += 1
    liste.append("\n")
    return liste


def plateau():
    ilan = 0
    liste_terrain = []
    while ilan < 6:
        liste_terrain.extend(liste_colone())
        liste_terrain.extend(liste_moins())
        ilan += 1
    return liste_terrain


def plateau_sans_ligne():
    ilan = 0
    liste_terrain = []
    while ilan < 6:
        liste_terrain.extend(liste_colone())
        ilan += 1
    return liste_terrain


def dico(ll):
    n = 0
    di = {}
    for x in ll:
        di[n] = x
        n += 1
    return di


def get_plateau_fini(liste):

    return print("".join(liste))
