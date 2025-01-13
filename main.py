
from fonctions import *
from regles import *


liste = plateau()
joueur = 0
j1 = "O"
j2 = "X"

while True:
    get_plateau_fini(liste)
    liste.reverse()
    place = input("Quelle position ?  ")

    for x in liste:
        if x == place:
            if joueur % 2 == 0:
                liste[liste.index(x)] = j1
                break
            else:
                liste[liste.index(x)] = j2
                break

    liste.reverse()
    dic = dico(liste)
    if gagner(dic) == True:
        print("C'est gagné !!!")
        break
    joueur += 1

