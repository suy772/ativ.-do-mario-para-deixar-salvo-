import random

print("~~ joguinho de pedra, papel e tesoura :3 ~~")
lista = ['papel', 'pedra', 'tesoura']
jogador_pontos = []
maquina_pontos = []

while True:
    jogador_pontos = 0
    maquina_pontos = 0
    jogador_pontos < 3 and maquina_pontos < 3 

    jogador = input("Escolha sua mão: ").lower()
    if jogador not in lista:
      print("Essa opção não existe, amigo.")
      continue
    maquina = random.choice(lista)
    print("a maquina jogou: ",(maquina))

    if jogador == maquina:
        print("deu empate :P")
        continue

    if (jogador == 'pedra' and maquina == 'tesoura') or \
       (jogador == 'papel' and maquina == 'pedra') or \
       (jogador == 'tesoura' and maquina == 'papel'):
       jogador = jogador_pontos =+ 1
       print(f"voce ganhouuuu 1 ponto :D. total --> {jogador}")

    else:
       maquina = maquina_pontos =+ 1
       print(f"a maquina ganhouuuu. total dela --> {maquina}")

    
