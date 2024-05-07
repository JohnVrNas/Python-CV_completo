import time
from random import randint
print('Hmmm... Estou pensando em um número entre 0 e 5')
time.sleep(1.25)
print('-=-'*13)
print('Você acha que consegue adivinhar?')
print('-=-'*13)
time.sleep(1.25)
print('Sim ou Não?')
r = str(input(': ')).upper().strip()
if r == 'SIM':
    print('Ok! Então vamos jogar!')
    time.sleep(1.25)
    print('Deixa eu pensar...')
    comp = randint(0, 5)
    time.sleep(1.25)
    player = int(input('Já sei! \nTenta a sorte!: '))
    if player == comp:
        print('Parabéns! Você conseguiu me vencer!')
    else:
        print('HAHAHAHAHA eu pensei no número {}, e não no {}'.format(comp, player))
else:
    print('Poxa... Queria tanto jogar...')




