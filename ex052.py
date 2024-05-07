print('='*15)
print('NÚMEROS PRIMOS')
print('='*15)
tot = 0
number = int(input('Digite um número: '))
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {number} foi divisível {tot} vezes')
if tot == 2:
    print(f'O número {number} \033[34mÉ PRIMO!\033[m')
else:
    print(f'O número {number} \033[31mNÃO É PRIMO! \033[m')





