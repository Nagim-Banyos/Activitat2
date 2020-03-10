import os
import sys

llista = os.listdir(os.path.join(os.path.dirname(__file__),"UNZIP"))
contador = 0
llistatFitxers={}
for i in llista:
    if i[1] == "5":
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
            print("------------")
            print("Codi provincia: " + linia[11:13])
            print("Nom municipi: " + linia[18:117])
            print("Codi ine municipi: " + linia[13:16])
            print("Distrito : " + linia[118:119])
except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
