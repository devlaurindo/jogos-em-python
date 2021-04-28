import adivinhacao
import forca

def escolhe_jogo():
    print ("***********************************")
    print ("******* Escolha o seu jogo! *******!")
    print ("***********************************")

    print ("\n (1) Adivinhação (2) Forca ")

    jogo = int (input ("\n Qual jogo? "))

    if (jogo == 1):
        print ("\n Jogando Adivinhação")
        adivinhacao.jogar()
    elif (jogo == 2):
        print ("\nJogando Forca")
        forca.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()