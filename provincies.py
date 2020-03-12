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

cnx = mysql.connector.connect(user='perepi', password='pastanaga',
                              host='10.93.255.122',
                              database='activitat2')
cursor = cnx.cursor()

try :
    with open(pathFitxer, "r") as fitxer:
        for linia in fitxer:
            if linia[11:13] != "99":
                stm_insert_provincies = ("INSERT INTO provincies"
                                            "(codi_ine, nom, comunitat_aut_id)"
                                            "VALUES (%s, %s, %s)")
                dades_provincies = (linia[11:13], linia[14:64], linia[11:13])
                cursor.execute(stm_insert_provincies,dades_provincies)
                cnx.commit()
            else:
                stm_insert_provincies = ("INSERT INTO provincies"
                                            "(codi_ine, nom, comunitat_aut_id)"
                                            "VALUES (%s, %s, %s)")
                dades_provincies = (linia[9:11], linia[14:64], linia[11:13])
                cursor.execute(stm_insert_provincies,dades_provincies)
                cnx.commit()

except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)
cursor.close()
cnx.close()
