import random

# número aleatório
number = random.randint(1, 100)

# número de tentativas
tries = 0
max_tries = 10

# laço principal
while tries < max_tries:
    # pede ao usuário um palpite
    guess = int(input("Digite um número entre 1 e 100: "))

    # verifica se o palpite está correto
    if guess == number:
        print("Parabéns, você acertou o número!")
        break

    # verifica se o palpite está muito alto
    if guess > number:
        print("O número é menor que", guess)

    # verifica se o palpite está muito baixo
    if guess < number:
        print("O número é maior que", guess)

    # incrementa o número de tentativas
    tries += 1

# verifica se o jogador perdeu todas as tentativas
if tries == max_tries:
    print("Você perdeu! O número era", number)
