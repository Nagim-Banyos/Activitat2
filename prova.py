import os
import zipfile

llista = os.listdir(os.path.join(os.path.dirname(__file__),"ZIPS"))

print (llista)


dirActual = os.path.join(os.path.dirname(__file__),"ZIPS")
print (dirActual)
nomFitxerZip = llista[0]
print (nomFitxerZip)
dirUnzip = os.path.join(os.path.dirname(__file__),"UNZIP")
pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
print (dirUnzip)
print(pathFitxerZip)

# Extraiem el contingut de pathFitxerZip a dirUnzip
with zipfile.ZipFile(pathFitxerZip, 'r') as zipRef:
    zipRef.extractall(dirUnzip)
