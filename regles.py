
from fonctions import *
import itertools


def gagner(dictionnaire):
    dico_de_base = dico(plateau())
    pos_j1 = []
    liste_tuple_1 = []
    liste_tuple_2 = []
    liste_tuple_3 = []
    pos_j2 = []
    for x in dictionnaire.keys():
        if dictionnaire[x] != dico_de_base[x]:
            if dictionnaire[x] == "O":
                pos_j1.append(x)
            if dictionnaire[x] == "X":
                pos_j2.append(x)

    if len(pos_j1) >= 4:
        for lol in itertools.combinations(pos_j1, 2):
            if lol[0] - lol[1] == 2 or lol[0] - lol[1] == -2:
                liste_tuple_1.append(lol)
            if lol[0] - lol[1] == 30 or lol[0] - lol[1] == -30:
                liste_tuple_2.append(lol)
            if lol[0] - lol[1] == 32 or lol[0] - lol[1] == -32:
                liste_tuple_3.append(lol)
        if len(liste_tuple_1) >= 3:
            return True
        if len(liste_tuple_2) >= 3:
            return True
        if len(liste_tuple_3) >= 3:
            return True

    liste_tuple_3 = []
    liste_tuple_1 = []
    liste_tuple_2 = []
    if len(pos_j2) >= 4:
        for lol in itertools.combinations(pos_j2, 2):
            if lol[0] - lol[1] == 2 or lol[0] - lol[1] == -2:
                liste_tuple_1.append(lol)
            if lol[0] - lol[1] == 30 or lol[0] - lol[1] == -30:
                liste_tuple_2.append(lol)
            if lol[0] - lol[1] == 32 or lol[0] - lol[1] == -32:
                liste_tuple_3.append(lol)
        if len(liste_tuple_1) >= 3:
            return True
        if len(liste_tuple_2) >= 3:
            return True
        if len(liste_tuple_3) >= 3:
            return True
