import os
os.system('cls')
def erro():
    vermelho = '\033[91m'
    endcolor = '\033[0m'
    print(vermelho+'ERRO! Digite um número inteiro válido'+ endcolor)


def leiaint(num):
    global user_input
    while True:
        user_input = input(num)
        if user_input.isnumeric():
            break
        elif user_input.strip() == '':
            erro()
        else:
            erro()

num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {user_input}')



