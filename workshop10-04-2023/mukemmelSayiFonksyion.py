

def mukemmelfonksiyon():

    sayi=int(input("Sayı Giriniz: "))
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i

    if toplam==sayi:
        print("Bu mükemmel sayıdır")
    else:
        print("Mükemmel sayı değildir")

mukemmelfonksiyon()
