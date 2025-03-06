import adivinhação
import velha

def escolha_jogos():
    print('************Lista de jogos************')
    print('Jogos: Jogo da velha[1], Jogo de adivinhação[2]')
    resp = int(input('Selecione um jogo para jogar: '))

    if resp == 1:
        velha.jogar()

    elif resp == 2:
        adivinhação.jogar()

if(__name__ == "__main__"):
    escolha_jogos()

