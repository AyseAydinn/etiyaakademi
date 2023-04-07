
# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

sayilar = []

for i in range(10):
    i= int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(i)


print(sayilar)
enBuyuk = max(sayilar)
enKucuk = min(sayilar)
print("Listedeki En Büyük Sayı : ", enBuyuk, "\nListedeki En Küçük Sayı : ", enKucuk)