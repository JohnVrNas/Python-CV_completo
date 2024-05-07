r = 0
tot18 = totm = toth = 0
while True:
    print('-'*10)
    print('CADASTRE UMA PESSOA')
    print('-' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('Acabou')
print(f'O total de pessoas com mais de 18 anos: {tot18}')
print(f'Temos ao todo {toth} homens cadastrados')
print(f'{totm} mulheres com menos de 20 anos estao cadastradas')


