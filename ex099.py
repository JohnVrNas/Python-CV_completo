import os
os.system('cls')
from time import sleep


def linha():
    print('-='*25)


def maior(*valores):
    if len(valores) == 0:
        linha()
        print('A sequência não possui números')
    else:
        linha()
        print('Analisando os valores passados...')

        for cada in valores:
            

            print(f'{cada} ', end='', flush=True)

            sleep(0.2)

        print(f'Foram informados {len(valores)} valores ao todo') 

        print(f'O maior valor informado foi {max(valores)}.')
  

# Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior()