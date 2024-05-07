import os
os.system('cls')
lista = []
resp ='S'
while resp in 'S':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta inválida... Tente novamente')
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('-='*40)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
