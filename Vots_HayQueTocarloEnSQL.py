import os
import sys

llista = os.listdir(os.path.join(os.path.dirname(__file__),"UNZIP"))
contador = 0
llistatFitxers={}
for i in llista:
    if i[1] == "3":
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
            #Default Vots_id
            print("Numero Vots: " + linia[22:30])
            #Default Candidatura_id

except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
