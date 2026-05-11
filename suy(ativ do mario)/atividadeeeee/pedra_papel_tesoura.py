import random

print("🪻୧﹒𝐣𝐨𝐠𝐮𝐢𝐧𝐡𝐨 : pedra, papel e tesoura﹒⌗")
lista = ['papel', 'pedra', 'tesoura']
jogador_pontos = 0
maquina_pontos = 0
while True:

    jogador = input(" ₊ ⊹ Escolha sua mão (˶˃ ᵕ ˂˶) !!  ✧˚. : ").lower().strip()
    if jogador not in lista:
        print("Essa opção não existe, amigo...(╥﹏╥)")
        break

    maquina = random.choice(lista)
    print("₊⊹ a maquina jogou: ",(maquina))

    if jogador == maquina:
        print("deu empate ( ˶°ㅁ°) !!")

    elif (jogador == 'pedra' and maquina == 'tesoura') or (jogador == 'papel' and maquina == 'pedra') or (jogador == 'tesoura' and maquina == 'papel'):
        jogador_pontos += 1
        print(f"✧˖°. voce ganhouuuu 1 ponto ( ˶˘ ³˘)♡. total --> {jogador_pontos}")
        print(" ")
    else:
        maquina_pontos += 1
        print(f"⟡ ݁₊ . a maquina ganhouuuu. total dela --> {maquina_pontos}")
        print(" ")

    if jogador_pontos == 3:
        print(f"o jogador ganhou com {jogador_pontos} pontos, parabensss ✧｡٩(ˊᗜˋ )و✧*｡")
        break
    if maquina_pontos == 3:
        print(f"a maquina ganhou com {maquina_pontos} pontos, bem feito (¬_¬)")
        break
