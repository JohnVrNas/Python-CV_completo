n = (int(input(f'Digite o 1° valor: ')),
     int(input(f'Digite o 2° valor: ')),
     int(input(f'Digite o 3° valor: ')),
     int(input(f'Digite o 4° valor: ')))
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3+1)}° posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')