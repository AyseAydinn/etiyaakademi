# döngüler - loops -start

# iterate etmek, iteration

for i in range(0,10):
    print(i)

ogrenciler = ["A1","B1","C1","D1","E1"]
#length
print(len(ogrenciler)) #listedeki eleman sayısını verir
# 5

#break => ilgili döngünün o anda kırılmasını (bitirilmesini) sağlar

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}. öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
for i in range(0,10):
    pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
for i in ogrenciler:
    if i=="C1": #ekrana C1 yazmadan devam eder.
        continue
    print(f"Öğrenci: {i}")


#while booleanDeger
#infinite loop - sonsuz döngü
#ctrl+c => terminali durdurur
i = 0
while i < 10:
    i = i + 1
    if i==3:
        break
    print(f"While içerisindeki i değeri: {i}")
    

# döngüler - loops -end