#!/usr/bin/env python3

import mysql.connector

mydb=mysql.connector.connect(
    host="mysql_db",
    port="3306",
    user="nicky",
    password="root",
    database="cryptoDB"
)
print(mydb)

crypto_data = open("crypto_data.csv","r")

line = crypto_data.readlines()

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE monnaies (ID int, Name VARCHAR(255), Symbol VARCHAR(255), Market_Cap VARCHAR(255), Price VARCHAR(255), Circulating_Supply VARCHAR(255), Volume VARCHAR(255), pourcentage_1h VARCHAR(255), pourcentage_24h VARCHAR(255), pourcentage_7j VARCHAR(255))")

for i in range (1,833):
    row = line[i].split(',')
    sql= "INSERT INTO monnaies (ID, Name, Symbol, Market_Cap, Price, Circulating_Supply, Volume, pourcentage_1h, pourcentage_24h, pourcentage_7j) VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
    mycursor.execute(sql,val)
    mydb.commit()
