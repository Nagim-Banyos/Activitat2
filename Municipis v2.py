llista = os.listdir(os.path.join(os.path.dirname(__file__), "UNZIP"))
print(llista)
contador = 0
llistatFitxers = {}
for i in llista:
    if i[1] == "5":
        contador += 1
        if i in llistatFitxers:
            print(i)
        else:
            llistatFitxers["fitxer" + str(contador)] = i
fitxer1 = llistatFitxers.get("fitxer1")
fitxer2 = llistatFitxers.get("fitxer2")

dirActual = os.path.dirname(__file__) + "/UNZIP" + "/" + fitxer1
print(dirActual)
pathFitxer = dirActual

cnx = mysql.connector.connect(user='root', password='patatilla',
                              host='34.230.175.156',
                              database='activitat2')
cursor = cnx.cursor()

try:
    with open(pathFitxer, "r") as fitxer:
        for linia in fitxer:
            stm_insert_municipi = ("INSERT INTO municipis"
                                   "(nom,codi_ine,provincia_id,districte)"
                                   "VALUES (%s,%s,%s,%s)")

            dades_municipi = (linia[18:117]), (linia[13:16]), (linia[11:13]), (linia[118:119])
            cursor.execute(stm_insert_municipi, dades_municipi)
            cnx.commit()

            '''print("------------")
            print("Codi provincia: " + linia[11:13])
            print("Nom municipi: " + linia[18:117])
            print("Codi ine municipi: " + linia[13:16])
            print("Distrito : " + linia[118:119])'''
except OSError as error:
    print("No s'ha pogut posar " + pathFitxer)