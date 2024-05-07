somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for per in range(1, 5):
    print('-'*5, f'{per}º PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F/OUTRO]: ')).upper().strip()
    somaidade += idade
    if per == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    if sexo == 'F' and idade < 20:
            totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')


