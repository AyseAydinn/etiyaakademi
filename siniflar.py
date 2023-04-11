# sınıflar => classlar


# self => this


class Human:

    #buit-in #constructor #initialize

    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self) -> str:
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")
    
# intance => örnek
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")