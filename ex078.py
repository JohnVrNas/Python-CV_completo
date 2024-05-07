import os 
os.system('cls')
valores = []
for cont in range (1, 6):
    valores.append(int(input(f'Digite o {cont}° valor: ')))
print('-='*25)
print(f'Você digitou os valores {valores}')
for pos, v in enumerate(valores):
    if v == max(valores):
        maior_pos = pos
        print(f'O maior valor é {max(valores)} na posição {pos}')
    if v == min(valores):
        menor_pos = pos
        print(f'O menor valor é: {min(valores)} na posição {pos}')
 