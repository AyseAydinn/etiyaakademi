sayilar = [100, 200, 300, 400, 500, "Merhaba", 15.5, True, "Merhaba"] #listedeki tüm elemanların veri tipi aynı olmak zorunda değil

#programcı saymaya 0'dan başlar
#index- indis => 0 Başlangıç değeri -1 son index
print(sayilar[0]) #ilk elemanı verir
print(sayilar[5]) #altıncı elemanı verir
print(sayilar)

sayilar.append(100)
sayilar.append(600) #listenin sonuna eleman ekler
print(sayilar)

sayilar.pop() #indexteki son elemanı siler.(içini boş bırakınca)
sayilar.pop(0) #0ıncı sıradaki indexi siler
print(sayilar)

sayilar.remove("Merhaba") #pop un aksine indexe göre değil değere göre siler.
#Listede birden fazla aynı değer varsa ilk sıradakini siler
print(sayilar)

sayilarEkleme =[100,700,800,900]
sayilar.extend(sayilarEkleme) #append in aksine tek bir değer değil listedeki tüm değerleri listeye ekler
print(sayilar) 

sayilar.clear() # dizinin içini boşaltan fokksiyon
print(sayilar)