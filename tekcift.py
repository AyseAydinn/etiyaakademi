
# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

# 2. geliştirdiğimiz programa kullanıcının alt limiti belirlemesi için gerekli desteği ekleyelim. 

ustlimit=int(input("Üst Limit Giriniz: "))
altlimit=int(input("Alt Limit Giriniz: "))


for ciftSayi in range(altlimit,ustlimit):
  if ciftSayi%2==0:
    print("Çift Sayilar : ", ciftSayi)

print("####################################")

for tekSayi in range(altlimit,ustlimit):
  if tekSayi%2!=0:
    print("Tek Sayilar : ", tekSayi)