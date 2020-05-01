import os
import zipfile

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

llista = os.listdir(os.path.join(os.path.dirname(__file__),"ZIPS"))
fitxer = llista[0]
descomprimirZIP(fitxer)