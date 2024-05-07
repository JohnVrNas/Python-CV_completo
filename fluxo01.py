import os
os.system('cls')
cont_mas = total_temp_fem = candidatos_2_e_4_anos = 0
for c in range(30):
    nome = str(input('Digite seu nome: ')).strip()
    print('-='*25)
    anos = int(input('Digite quantos anos de experiência você tem na área: '))
    print('-='*25)
    while anos < 0:
        print('Número inválido... Digite novamente')
        anos = int(input('Digite quantos anos de experiência você tem na área: '))
    sexo = str(input('Digite seu sexo biológico [M/F]: ')).upper().strip()[0]
    print('-='*25)
    while sexo not in 'MF':
        print('Sexo inválido... Tente novamente')
        sexo = str(input('Digite seu sexo biológico [M/F]: ')).upper().strip()[0]
        print('-='*25)
    if sexo == 'M':
        cont_mas += 1
    elif sexo == 'F':
        total_temp_fem += anos
    if 2 >= anos <= 4:
        candidatos_2_e_4_anos += 1
tempo_feminino  = total_temp_fem / (30-cont_mas)
percent_e_4_5 = (candidatos_2_e_4_anos/30) * 100
print(f"a) Quantidade de candidatos do sexo masculino: {cont_mas}")
print(f"b) Média do tempo de experiência das candidatas do sexo feminino: {tempo_feminino:.2f}")
print(f"c) Percentual de candidatos com tempo de experiência entre 2 e 4 anos: {percent_e_4_5:.2f}%")