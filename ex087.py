import os
os.system('cls')
pares = col3 = 0
num = [[0,0,0],[0,0,0,],[0,0,0]]
for l in range(0,3):
    for c in range(0, 3):
        num[l][c] = (int(input(f'Digite um valor para [{l}], [{c}]: ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{num[l][c]:^5}]', end='')
        if num[l][c] % 2 == 0:
            pares += num[l][c]
    print()
for l in range(0, 3):
  col3 += num[l][2]
print('-' * 35, f'\nA soma dos números pares é {pares}')
print(f'A soma dos números da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {max(num[1])}')