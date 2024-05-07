import os
os.system('cls')
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >=0 and n<=20:
        break
    print('Número Inválido... Tente novamente')
print(f'Você digitou o número {cont[n]}')


