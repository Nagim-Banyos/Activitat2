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
            print(linia[2:8])
            print(linia[2:6])
            print(linia[6:9])
            print(linia[0:11])

except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
