#!/usr/bin/env python3


crypto_data = open("crypto_data.csv","r")

line = crypto_data.readlines()
row = line[0].split(',')
for i in range(10):
    print(row[i])

print("je suis python")
