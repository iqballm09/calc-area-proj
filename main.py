import sys
import time
import tkinter as tk

from module.luas import *


# Function
def list_bangun2D():
    print("Pilih bangun :")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Trapesium")
    print("6. Quit the program")


def luasBangun(ans1):
    if ans1 == 1:
        obj = Persegi()
        obj.getSisi()
        obj.countLuas()
        obj.printLuas()
    elif ans1 == 2:
        obj = PersegiPanjang()
        obj.getPanjangLebar()
        obj.countLuas()
        obj.printLuas()
    elif ans1 == 3:
        obj = Segitiga()
        obj.getSisi()
        obj.countLuas()
        obj.printLuas()
    elif ans1 == 4:
        obj = Lingkaran()
        obj.getRadius()
        obj.countLuas()
        obj.printLuas()
    elif ans1 == 5:
        obj = Trapesium()
        obj.getSisi()
        obj.countLuas()
        obj.printLuas()
    else:
        pass


# Screen
time.sleep(2)
condition = True
print("==========================================================================")
print(" Area Calculator : Program untuk menghitung luas dari suatu bangun datar. ")
print("==========================================================================")
print("Note : Presisi yang dihasilkan sebatas 3 angka dibelakang koma.")
while condition:
    cond2 = True
    print()
    list_bangun2D()
    while cond2:
        try:
            ans1 = int(input("Your Option : "))
            assert ans1 in list(range(1, 7))
            print()
            luasBangun(ans1)
            cond2 = False
        except ValueError:
            print("Input dengan angka!")
        except AssertionError:
            print("Input masukan tidak ada di pilihan!")

    # Untuk cek apakah masih melanjutkan program
    cond4 = True
    while cond4:
        try:
            ans4 = input("Quit the program (y/n)? : ")
            assert ans4.upper() == "Y" or ans4.upper() == "N"
            if ans4.upper() == "Y":
                condition = False
            cond4 = False
        except:
            print("Input dengan 'Y/y' atau 'N/n'")
