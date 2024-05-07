import os
os.system('cls')
num = [[],[]]
for cont in range(1,8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')
