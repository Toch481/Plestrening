import random

print("Zahraj si semnou kámen nůžky, papír!")

tah_cloveka = input("Zadej kámen, nůžky nebo papír. ")
moznosti = {1: "kámen", 2: "nůžky", 3: "papír"}
tah_pocitace = moznosti[random.randint(1, 3)]

print(tah_pocitace)

if tah_cloveka == tah_pocitace:
    print("Plichta!")
elif (tah_cloveka == "nůžky" and tah_pocitace == "kámen") or (tah_cloveka == "papír" and tah_pocitace == "nůžky") or (tah_cloveka == "kámen" and tah_pocitace == "papír"):
    print("Počítač vyhrál!")
elif (tah_cloveka == "nůžky" and tah_pocitace == "papír") or (tah_cloveka == "papír" and tah_pocitace == "kámen") or (tah_cloveka == "kámen" and tah_pocitace == "nůžky"):
    print("Vyhrála jsi!")
else:
    print("Špatně.")
    tah_cloveka = input("Zadej jedno ze slov: kámen, nůžky nebo papír a dej si pozor na diakritiku. ")
