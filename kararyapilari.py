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


print("-----------------------------------------------------")


studentCount = 44
if studentCount > 20:
    print("Öğrenciler ders için hazır")

print("-----------------------------------------------------")

vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 
print("Ortalama: ", ortalama, "\nVize: ", vize,  "\nFinal: ", final)

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

#condition-logic
# or and
# (true or false) => true => sol ve sağındaki koşullardan en az birisinin true olmasını istiyor 
# (true and false) => false => sol ve sağındaki koşulların ikisinin de kesinlikle true olmasını ister

if (final < 40) or (ortalama < 50) or (vize == final *2):
    print("Kaldı")
# elif ortalama < 50:
#     print("Kaldı")
# elif vize == final * 2:
#     print("Kaldı")
else:
    print("Geçti")
