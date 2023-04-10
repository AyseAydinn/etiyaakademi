    
def sayilar():
    ustlimit=int(input("Üst Limit Giriniz: "))
    altlimit=int(input("Alt Limit Giriniz: "))


    for ciftSayi in range(altlimit,ustlimit):
        if ciftSayi%2==0:
            print("Çift Sayilar : ", ciftSayi)
sayilar()