# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:51:57 2024

@author: Lenovo
"""

skor = 0 
nilaimurid = list() 
ulang = 0 
nomor = 0

while ulang == 0: 
    nomor += 1 
    x = str(input("masukan nilai: "))

    if x == 'selesai': 
        ulang = 1
    else:

        if x == 'A': 
            skor = float(4.00)

        elif x== 'A-': 
            skor = float(3.75)

        elif x== 'B+': 
            skor = float(3.50)

        elif x== 'B': 
            skor = float(3.00)

        elif x== 'B-': 
            skor = float(2.75)

        elif x== 'C+': 
            skor = float(2.50)

        elif x== 'C': 
            skor = float(2.00)

        elif x== 'C-': 
            skor = float(1.75)

        elif x == 'D': 
            skor = float(1.50)

        elif x == 'E':
            skor = float(1.25)

        else:
            print('Saya tidak mengerti...')
            skor = 0
        print(('\nNilai ke-{0} = {1}').format(nomor, skor))
        nilaimurid.append(skor)

rata2 = sum(nilaimurid) / len (nilaimurid)
print('rata rata nilai murid tersebut:', rata2)