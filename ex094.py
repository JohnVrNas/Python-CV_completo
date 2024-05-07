import os
os.system('cls')
dados = list()
info = dict()
resp = 'S'
while resp == 'S':
    info.clear()

    info['nome'] = str(input('Nome: ')).strip()


    info['sexo'] = str(input('Sexo [M/F]: '))[0].strip().upper()
    while info['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        info['sexo'] = str(input('Sexo [M/F]: '))[0].strip().upper()
    
    info['idade'] = int(input('Idade: '))

    dados.append(info.copy())
    

    resp = str(input('Quer continuar?: ')).upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas Sim ou Não')
        resp = str(input('Quer continuar?: ')).upper()[0]
        if resp == 'N':
            break
    os.system('cls')

print('-='*40)

soma_idades = sum((pessoa['idade']) for pessoa in dados)
media_idades = soma_idades / len(dados)

# quantidade de pessoas cadastradas
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')

# média da idade das pessas cadastradas
print(f'B) Média das idades: {media_idades:.2f} anos')

# Lista de mulheres cadastradas
print(f'C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')

print(f'D) Lista de pessoas com idade acima da média: ')
for p in dados:
    if p['idade'] >= media_idades:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >> ')




