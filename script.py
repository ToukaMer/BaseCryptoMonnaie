#!/usr/bin/env python3

import mysql.connector

mydb=mysql.connector.connect(
    host="mysql_db",
    port="8080",
    user="nicky",
    password="root"
)
print(mydb)

crypto_data = open("crypto_data.csv","r")

line = crypto_data.readlines()
row = line[0].split(',')
for i in range(10):
    print(row[i])

print("je suis python")
