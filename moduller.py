#alias =>takma ad => m
# import matematik as m # matematik modülünü import etti
from matematik import topla as toplamaİslemi # Sadece matematik modülünün içindeki topla fonksiyonunu import etti
from siniflar import Human # siniflar modülünün içindeki Human classını import etti.

#built-in modules

import random #python içindeki random modülünü import etti

print(toplamaİslemi(10,20))

print(random.randint(0,100)) # 0(dahil) ile 100(dahil) arasında rastgele sayı üretir.

Human1 = Human("Mirza")
Human1.talk("Merhaba")