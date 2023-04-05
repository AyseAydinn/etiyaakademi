#değişkenler - start
baslik = 'HABERİNİZ OLSUN'  #string
vade = 12  #integer
faizOrani = 1.47  #float

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani))

mesaj = "Hoşgeldin"
musteriAdi = "Ayşe"
musteriSoyadi = "Aydin"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"

print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)

print(sonucMesaj)
#değişkenler - end

#şart blokları - start
dolarDun = 7.65
dolarBugun = 7.75

if dolarDun > dolarBugun:
  print("Azalış oku")
  print("Bitti")
elif dolarDun < dolarBugun:
  print("Artış oku")
else:
  print("Eşittir oku")

print("Bitti")
#şart blokları - end

#listeler - start
krediler = [
  "Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel",
  "Mutlu emekli ihtiyaç kredisi"
]

print(krediler)
print(krediler[0])  #diziler sıfırıncı elemandan başlar
print(krediler[1])
print(krediler[2])

print(len(krediler))  #length - dizideki eleman sayısını verir

krediler[
  0] = "Çabuk kredi"  #dizideki sıfırıncı eleman olan hızlı krediyi çabuk kredi olarak değiştirdi
print(krediler)
#listeler - end

#ldöngüler - start
krediler = [
  "Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel",
  "Mutlu emekli ihtiyaç kredisi"]

#kredi -> alias
for kredi in krediler:
  print(kredi)

#range -> alias
for i in range(10):  #0'dan başlar 10 dahil değil
  print(i)

for i in range(
    len(krediler)
):  #krediler listesinin uzunluğu kadar -> 0'dan 3'e kadar 3 dahil değil
  print(krediler[i])

for i in range(3, 10):  #3'ten başlar 10 dahil değil
  print(i)

for i in range(0, 10, 2):  #0'dan başlar 10 dahil değil 2'şer artar.
  print(i)

for kredi in krediler:
  print("<option>"+kredi+"<option>")
#ldöngüler - end


  
#fonksiyonlar - start
def kredileriListele():
  krediler = [
  "Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel",
  "Mutlu emekli ihtiyaç kredisi"]
  for kredi in krediler:
    print("<option>"+kredi+"<option>")

kredileriListele()
kredileriListele();
kredileriListele();
kredileriListele();

#fonksiyonlar - end
