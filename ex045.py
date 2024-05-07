from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print('O Computador jogou {}'.format(itens[pc]))
if pc == 0:
    if jogador == 0:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('EMPATE!')
    elif jogador == 1:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ PERDEU!')
    elif jogador > 2:
        print('JOGADA INVÁLIDA')

elif pc == 1:

    if jogador == 0:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('EMPATE!')
    elif jogador == 2:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ GANHOU!')
    elif jogador > 2:
        print('JOGADA INVÁLIDA')

elif pc == 2:
    if jogador == 0:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('O Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        print('EMPATE!')
    elif jogador > 2:
        print('JOGADA INVÁLIDA')
