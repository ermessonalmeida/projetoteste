print(
    """Opões de jogada:
[0] Pedra
[1] Papel
[2] Tesoura
"""
)
computador = int(input("Insira sua jogada computador!: "))
jogador = int(input("Insira sua jogada Jogador!: "))

if computador == 0 and jogador == 0:
    print("Jogada Empatada")
    print(" haaa Não Desista")
if computador == 1 and jogador == 0:
    print("Jogador Perdeu")
    print(" haaa Não Desista")
if computador == 2 and jogador == 0:
    print("Jogador venceu")
    print("Parabéns!")
if computador == 0 and jogador == 1:
    print("Jogador Ganhou")
    print("Parabéns!")
if computador == 1 and jogador == 1:
    print("Jogada Empatada")
    rint(" haaa Não Desista")
if computador == 2 and jogador == 1:
    print("Jogador Venceu")
    print("Parabéns!")
if computador == 0 and jogador == 2:
    print("Jogador Perdeu")
    print(" haaa Não Desista")
if computador == 1 and jogador == 2:
    print("Jogador Ganhou")
    print("Parabéns!")
if computador == 2 and jogador == 2:
    print("Jogada Empatada")
    print("Não Desista tente Novamente")
elif computador != 0:
    if computador != 1:
        if computador != 1:
            print("Jogue Novamente")
elif jogador != 0:
    if jogador != 1:
        if jogador != 2:
            print("Jogue Novamente")

