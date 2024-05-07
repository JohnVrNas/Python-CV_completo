import os
os.system('cls')
valores = []
resp = ''
while resp != 'N':
    numeros = int(input('Digite um valor: '))
    if numeros not in valores:
        valores.append(numeros)
    else:
        print('Valor duplicado')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print(f'Você digitou os valores {sorted(valores)}')
