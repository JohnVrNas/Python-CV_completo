import os
os.system('cls')
global vermelho 
vermelho = '\033[91m' 

global endcolor 
endcolor = '\033[0m'

def erroreal():
    print(vermelho+'ERRO! por favor, Digite um número inteiro válido'+ endcolor)
    return 0

def erroint():
    print(vermelho+'ERRO! por favor, Digite um número real válido'+ endcolor)


def leiaint(num):
    while True:
        try:
            num = int(input(num))
        except (ValueError, TypeError):
            erroint()
            continue
        except (KeyboardInterrupt):
            print(vermelho+'Entrada de dados interrompida pelo usuário.'+endcolor)
            return 0 
        else:
            return num
        
def leiafloat(num2):
    while True:
        try:
            num2 = float(input(num2))
        except(ValueError, TypeError):
            erroreal()
            continue
        except (KeyboardInterrupt):
            print(vermelho+'Entrada de dados interrompida pelo usuário.'+endcolor)
            return 0
        else:
            return num2
    
num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')

print(f'Você acabou de digitar o número inteiro {num} e o número real {num2}')
