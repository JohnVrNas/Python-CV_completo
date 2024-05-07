import os
from random import randint
os.system('cls')
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando {len(lista)} valores da lista: ', end='')
    for cada in lista:
        print(cada, end=', ')
    print('==> FIM!')

def somaPar(lista): 
    par = list()
    for cada in lista:
        if cada % 2 == 0:
            par.append(cada)
    print(f'Somando os valores pares de {numeros}, temos {sum(par)}')


numeros = list()
sorteia(numeros)
somaPar(numeros)