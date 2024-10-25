# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:37:15 2024

@author: Lenovo
"""

def hitung_harga(umur):
    if umur <= 2:
        return 0  
    elif umur <= 12:
        return 14  
    elif umur <= 64:
        return 23  
    else:
        return 18  

def main():
    print("=====SELAMAT DATANG DI KEBUN BINATANG TRISAKTI=====")
    running_total = 0
    
    while True:
        umur = int(input("masukkan umur: "))
        if umur == -1:
            break
        harga = hitung_harga(umur)
        if harga == 0:
            print("Gratis")
        else:
            print(f"Harga: ${harga}")
        running_total += harga
        print(f"Running total: ${running_total:.2f}")
    jumlah_uang = float(input("masukkan jumlah uang: "))
    kembalian = jumlah_uang - running_total
    print(f"Running Kembalian: ${kembalian:.2f}")
    print("=====TERIMAKASIH=====")

main()