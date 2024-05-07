import time
from random import randint
comp = randint(0, 5)
rsp = 0
tot = 0
player = 0
print('Hmmm... Estou pensando em um número entre 0 e 10')
#time.sleep(1)
print('-=-'*13)
print('Você acha que consegue adivinhar?')
print('-=-'*13)
#time.sleep(1)
print('Sim ou Não?')
r = str(input(': ')).upper().strip()
if r == 'SIM':
    print('Ok! Então vamos jogar!')
    #time.sleep(1)
    print('Deixa eu pensar...')
    rsp = int(input('Já sei! \nTenta a sorte!: '))
    #time.sleep(1)
    while rsp != comp:
        rsp = int(input(': '))
        if rsp == comp:
            print('Parabéns! Você conseguiu me vencer!')
            rsp += 1 - 1
    print(f'Para ganhe de mim você teve que tentar {rsp} vezes')
else:
    print('Poxa... Queria tanto jogar...')

