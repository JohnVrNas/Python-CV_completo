import os
from uteis import numeros
os.system('cls')
num = int(input('Digite um número para ver seu fatorial: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')