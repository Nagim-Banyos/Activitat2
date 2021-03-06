import os
import sys
import mysql.connector

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

cnx = mysql.connector.connect(user='root', password='patatilla',
                              host='34.230.175.156',
                              database='activitat2')
cursor = cnx.cursor()

try :
    with open(pathFitxer, "r") as fitxer:
        for linia in fitxer:
            if linia[11:13] == "99":
                if linia[9:11] != "99":
                    stm_insert_comunitats = ("INSERT INTO comunitats_autonomes"
                                             "(codi_ine, nom)"
                                             "VALUES (%s, %s)")
                    dades_com_aut = (linia[9:11], linia[14:64])
                    cursor.execute(stm_insert_comunitats, dades_com_aut)
                    cnx.commit()
except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
cursor.close()
cnx.close()
