vize = float(input("Vize Notu: "))
final = float(input("Final Notu: "))
ortalama = (vize * 0.4) + (final * 0.6)

if ortalama <= 49:
    print("Ortalama: ", ortalama , "Harf Notu: FF")
if (ortalama >= 50) and (ortalama<=59):
    print("Ortalama: ", ortalama , "Harf Notu: DD")
if (ortalama >= 60) and (ortalama<=69):
    print("Ortalama: ", ortalama , "Harf Notu: CC")
if (ortalama >= 70) and (ortalama<=79):
    print("Ortalama: ", ortalama , "Harf Notu: BB")
if (ortalama >= 80) and (ortalama<=100):
    print("Ortalama: ", ortalama , "Harf Notu: AA")