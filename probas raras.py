import zipfile
import os

dirActual = os.path.join(os.path.dirname(__file__),"ZIPS")
print (dirActual)
nomFitxerZip = "02197706_MESA.zip"
dirUnzip = os.path.join(os.path.dirname(__file__),"UNZIP")
pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
print (dirUnzip)

# Extraiem el contingut de pathFitxerZip a dirUnzip
with zipfile.ZipFile(pathFitxerZip, 'r') as zipRef:
    zipRef.extractall(dirUnzip)


