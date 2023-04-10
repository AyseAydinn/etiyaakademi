
def fibonacciFonksiyon():

    fibonacciList = []
    birinciSayi = 0
    ikinciSayi = 1

    fibonacciList.append(birinciSayi)
    fibonacciList.append(ikinciSayi)

    alinanSayi=int(input("Merhaba 20 veya 20'den büyük bir sayi giriniz: "))

    if(alinanSayi<20):
        print("Yanlış değer girdiniz !! Lütfen 20 veya 20'den büyük bir sayı giriniz.")

    else:
        for i in range(alinanSayi):

            ucuncuSayi = birinciSayi + ikinciSayi
            birinciSayi = ikinciSayi
            ikinciSayi = ucuncuSayi

            fibonacciList.append(ucuncuSayi)
        print(fibonacciList)

fibonacciFonksiyon()


