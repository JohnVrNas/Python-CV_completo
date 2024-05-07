import os
os.system('cls')
pessoas = []
dados = []
resp = 'S'
mai = men = 0
while resp not in 'N':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('Resposta inválida...Tente novamente')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'a) Ao todo,você cadastrou {len(pessoas)} pessoas')
print(f'b) O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]',end=' ')
print(f'c) O menor peso foi de {men}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]',end=' ')