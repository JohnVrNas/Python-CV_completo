from math import factorial
n1 = int(input('Digite um número para saber seu fatorial: '))
c = n1
f = factorial(n1)
print(f'Calculando {n1}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)

