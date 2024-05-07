import os
os.system('cls')
import bisect
numbers = []
for i in range(5):
    n = int(input('Digite um número: '))
    bisect.insort(numbers, n)
    print(f'Número {n} colocado na posição {numbers.index(n)}')
print(f'Números escritos: {numbers}')