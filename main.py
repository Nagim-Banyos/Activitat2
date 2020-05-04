import os
import mysql.connector
import zipfile

def llistarZIPS():
    llista = os.listdir(os.path.join(os.path.dirname(__file__),"ZIPS"))
    return llista

def descomprimirZIP(fitxer):
    dirActual = os.path.join(os.path.dirname(__file__),"ZIPS")
    print (dirActual)
    nomFitxerZip = fitxer
    dirUnzip = os.path.join(os.path.dirname(__file__),"UNZIP")
    pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
    print (dirUnzip)

    # Extraiem el contingut de pathFitxerZip a dirUnzip
    with zipfile.ZipFile(pathFitxerZip, 'r') as zipRef:
        zipRef.extractall(dirUnzip)

def introduirComunitatsAutonomes():
    llista = os.listdir(os.path.join(os.path.dirname(__file__), "UNZIP"))
    contador = 0
    llistatFitxers = {}
    for i in llista:
        if i[1] == "7":
            contador += 1
            if i in llistatFitxers:
                print(i)
            else:
                llistatFitxers["fitxer" + str(contador)] = i
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

    try:
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

def introduirMunicipis():
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

                dades_municipi = (linia[18:117]),(linia[13:16]),(linia[11:13]),(linia[118:119])
                cursor.execute(stm_insert_municipi,dades_municipi)
                cnx.commit()

                '''print("------------")
                print("Codi provincia: " + linia[11:13])
                print("Nom municipi: " + linia[18:117])
                print("Codi ine municipi: " + linia[13:16])
                print("Distrito : " + linia[118:119])'''
    except OSError as error:
        print("No s'ha pogut posar " + pathFitxer)

def tractarFitxer():
    # importar comunitats autonomes 07
    introduirComunitatsAutonomes()

    # importar provincies 07
    # importar municipis 05
    introduirMunicipis()
    # importar candidatures 03
    pass

tractarFitxer()

'''Això seria el programa principal
for fitxer in llistarZIPS():
    # descomprimirZIP(fitxer)
    # tractarFitxer()
    #esborrarzipdescomprimit
    '''

'''while contadorZIPS < len(llista):
    print(llista[contadorZIPS])
    contadorZIPS+=1
'''
