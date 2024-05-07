import os
os.system('cls')
n = []
n_pares = []
n_impares = []
resp = 'S'
while resp == 'S':
    n.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta inválida...Tente novamente')
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('-='*40)
print(f'A lista completa é {n}')
for i in n:
    if i % 2 == 0:
        n_pares.append(i)
    else:
        n_impares.append(i)
print(f'A lista de pares é {n_pares}')
print(f'A lista de ímpares é {n_impares}')
