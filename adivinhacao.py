import random

def jogar():
    print ("*********************************")
    print ("Bem vindo ao jogo de adivinhação!")
    print ("*********************************")

    # Variaveis do jogo
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    # Interação com o jogador para a escolha do nivel
    print ("\nQual nível de dificuldade?\n")
    print ("(1) Fácil (2) Médio (3) Difícil\n")

    # Variavel intermediaria para definir o total de jogadas
    nivel = int (input ("Define o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Laço de repetição para as tentativas
    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}". format(rodada, total_de_tentativas))

    # Onde o jogador faz o chute do número aleatorio
        chute_str = input ("\nDigite o seu numero entre 1 e 100: ")
        print ("Você digitou", chute_str)
        chute = int (chute_str)

        if (chute < 1 or chute > 100):
            print ("\nVocê deve digitar um número entre 1 e 100!\n")
            continue

    # Condições de como vai dar a dica para o jogador
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    # Resposta se ele acertou ou não acertou o numero
        if (acertou):
            print ("Você acertou e fez {} pontos\n".format(pontos))
            break
        else:
            if (maior):
                print ("Você errou! O seu chute for maior do que o número secreto\n")
            elif (menor):
                print ("Você errou! O seu chute for menor do que o número secreto\n")
                pontos_perdidos = abs(numero_secreto - chute) # Vai Calcular o pontos perdidos e a função abs server para sempre deixa o numero positivo
                pontos = pontos - pontos_perdidos


    print ("Fim do jogo")

if (__name__ == "__main__"):
    jogar()