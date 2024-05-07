import os
os.system('cls')

roxo = '\033[95m'
azul = '\033[94m'
verde = '\033[92m'
laranja = '\033[93m'
vermelho = '\033[91m'
endcolor = '\033[0m'

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', laranja)
    print(roxo, end='')
    help(com)
    print(endcolor, end='')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(verde, end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(endcolor, end='')
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print(verde+'ATÉ LOGO'+endcolor)