import os
import sys

llista = os.listdir(os.path.join(os.path.dirname(__file__),"UNZIP"))
contador = 0
llistatFitxers={}
for i in llista:
    if i[1] == "7":
        contador+=1
        if i in llistatFitxers:
            print(i)
        else:
            llistatFitxers["fitxer"+str(contador)] = i
print(llistatFitxers)
fitxer1 = llistatFitxers.get("fitxer1")
fitxer2 = llistatFitxers.get("fitxer2")

dirActual = os.path.dirname(__file__) + "/UNZIP" + "/" + fitxer1
print(dirActual)
pathFitxer = dirActual


try :
    with open(pathFitxer, "r") as fitxer:
        for linia in fitxer:
            #Default
            print("Eleccions" + linia[2:9])
            #Calculado de DATA sacas el [2:6] de la linia
            #Calculado de DATA sacas el [6:9] de la linia
            print(linia[6:9] + "/" + linia[2:6])


except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
