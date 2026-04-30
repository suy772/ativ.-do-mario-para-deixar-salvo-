vc = input("escolha entre pedra, papel e tesoura: ")
import random
lista = ["pedra", "papel", "tesoura"]
escolha = random.choice(lista)
print(escolha)
while true:
    if vc == escolha:
        print("voce perdeu")
# eu vou surtarrrrrr
