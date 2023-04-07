ortalamaNot = input("Lütfen ortalamanızı giriniz: ")

#numerik => int, double
ortalamaNotAsInteger = int(ortalamaNot) #type conversion

#if else blokları
#4 satır => 1 tab/indent

if ortalamaNotAsInteger > 80:
    print("Bravo")

elif ortalamaNotAsInteger > 60:
    print("Ortalama")

elif ortalamaNotAsInteger >50:
    print("Normal")

else:
    print("Malesef")
    print("Kaldınız")


