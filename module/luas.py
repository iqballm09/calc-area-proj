import math


class PersegiPanjang:

    def __init__(self):
        self.cond = True

    def getPanjangLebar(self):
        while self.cond:
            try:
                inp1 = float(input("Panjang (cm): "))
                inp2 = float(input("Lebar (cm): "))
                self.__panjang = inp1
                self.__lebar = inp2
                self.cond = False
            except:
                print("Input dengan format angka(int or float)!")

    def countLuas(self):
        self.__luas = self.__panjang * self.__lebar

    def printLuas(self):
        print("Luas Persegi Panjang dengan Panjang", self.__panjang, "cm", "dan Lebar", self.__lebar,
              "cm adalah", round(self.__luas, 2), "cm^2.")


class Persegi:

    def __init__(self):
        self.cond = True

    def getSisi(self):
        while self.cond:
            try:
                inp = float(input("Sisi (cm): "))
                self.__sisi = inp
                self.cond = False
            except:
                print("Input dengan format angka(int or float)!")

    def countLuas(self):
        self.__luas = self.__sisi * self.__sisi

    def printLuas(self):
        print("Luas Persegi dengan panjang sisi", self.__sisi,
              "adalah", round(self.__luas, 3), "cm^2.")


class Segitiga:
    # Heron's Formula
    def __init__(self):
        self.cond = True

    def getSisi(self):
        while self.cond:
            try:
                inp1 = float(input("Sisi 1 (cm): "))
                inp2 = float(input("Sisi 2 (cm): "))
                inp3 = float(input("Sisi 3 (cm): "))
                self.__a = inp1
                self.__b = inp2
                self.__c = inp3
                self.cond = False
            except:
                print("Input dengan format angka(int or float)!")

    def countLuas(self):
        self.__total = self.__a + self.__b + self.__c
        self.__luas = math.sqrt(self.__total*(self.__total - self.__a)
                                * (self.__total - self.__b)*(self.__total - self.__c))

    def printLuas(self):
        print("Luas Segitiga dengan masing-masing panjang sisi", self.__a, "cm,", self.__b, "cm,", self.__c,
              "cm adalah", round(self.__luas, 3), "cm^2.")


class Lingkaran:
    def __init__(self):
        self.cond = True

    def getRadius(self):
        while self.cond:
            try:
                inp = float(input("Panjang jari-jari (cm): "))
                self.__r = inp
                self.cond = False
            except:
                print("Input dengan format angka(int or float)!")

    def countLuas(self):
        self.__luas = math.pi * self.__r * self.__r

    def printLuas(self):
        print("Luas Lingkaran dengan Jari-jari", self.__r,
              "cm adalah", round(self.__luas, 3), "cm^2.")


class Trapesium:
    # Heron's Formula
    def __init__(self):
        self.cond = True

    def getSisi(self):
        while self.cond:
            try:
                inp1 = float(input("Panjang sisi bawah (cm): "))
                inp2 = float(input("Panjang sisi atas (cm): "))
                inp3 = float(input("tinggi (cm): "))
                self.__s1 = inp1
                self.__s2 = inp2
                self.__t = inp3
                self.cond = False
            except:
                print("Input dengan format angka(int or float)!")

    def countLuas(self):
        self.__luas = (self.__s1 + self.__s2) * self.__t / 2

    def printLuas(self):
        print("Luas Trapesium dengan panjang sisi bawah, sisi atas dan tinggi", self.__s1, "cm,", self.__s2, "cm,", self.__t,
              "cm adalah", round(self.__luas, 3), "cm^2.")
