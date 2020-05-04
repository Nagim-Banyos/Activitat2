import mysql.connector

cnx = mysql.connector.connect(user='root', password='patatilla',
                              host='34.230.175.156',
                              database='activitat2')
cursor = cnx.cursor()

query = ("SELECT comunitat_aut_id, nom, codi_ine"
         "      FROM comunitats_autonomes")

cursor.execute(query)

for (comunitat_aut_id, nom, codi_ine) in cursor:
    print(comunitat_aut_id,nom,codi_ine)

cursor.close()
cnx.close
