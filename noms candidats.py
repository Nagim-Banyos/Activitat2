import os
import sys

llista = os.listdir(os.path.join(os.path.dirname(__file__),"UNZIP"))
contador = 0
llistatFitxers={}
for i in llista:
    if i[1] == "4":
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
            persones=[]
            persona =(linia[25:100])
            persona = persona.split(" ")
            for i in persona:
                if i != "":
                    persones.append(i)
            print(persones)


            #importar persones[0:] = nom
            #importar persones[-1:] = 2 cognom
            #importar persones[1:-2] = 1 cognom
            

except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
