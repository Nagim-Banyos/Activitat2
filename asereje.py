import mysql.connector

cnx = mysql.connector.connect(user='perepi', password='pastanaga',
                              host='10.93.255.122',
                              database='activitat2')
cnx.close()
