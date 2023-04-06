sayi1 = float(input("Birinci Sayı :"))
sayi2 = float(input("İkinci Sayi :"))

print("###########################################################")
print("Yapmak istediğiniz hesaplama için işlem seçiniz!!!")
print("###########################################################")

islemSec = input("Toplama (+), Çıkarma (-), Çarpma (*), Bölme(/)")

if islemSec == "+":
    print("sonuç =" , sayi1 + sayi2)

elif islemSec == "-":
    print("sonuç =" , sayi1 - sayi2)

elif islemSec == "*":
    print("sonuç =" , sayi1 * sayi2)

elif islemSec == "/":
    print("sonuç =" , sayi1 / sayi2)
else:
    print("Lütfen dört işlemden birini seçiniz!!!")
