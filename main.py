import os
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

def tractarFitxer():
    # importar comunitats autonomes 07
    # importar provincies 07
    # importar municipis 05
    # importar candidatures 03
    pass


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
