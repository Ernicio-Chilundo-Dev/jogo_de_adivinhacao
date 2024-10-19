import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    jogar_novamente = True

    while jogar_novamente:
        numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        tentativas = 0
        max_tentativas = 5
        print("\nAdivinhe um número entre 1 e 100. Você tem 5 tentativas.")

        while tentativas < max_tentativas:
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print("Muito alto! Tente novamente.")

            if tentativas == max_tentativas:
                print(f"Você não conseguiu adivinhar o número em {max_tentativas} tentativas. O número era {numero_secreto}.")

        # Verificar se o jogador quer jogar novamente
        jogar_novamente_input = input("Deseja jogar novamente? (S/N): ").lower()
        if jogar_novamente_input != "s":
            jogar_novamente = False
            print("Obrigado por jogar! Até a próxima.")

# Iniciar o jogo
jogo_adivinhacao()
