import os
os.system('cls')
dados = {}
dados['nome'] = str(input('Digite o nome do aluno: ')).strip()
nota1 = float(input(f'Digite a primeira nota de {dados["nome"]}: '))
nota2 = float(input(f'Digite a segunda nota de {dados["nome"]}: '))
dados['media'] = (nota1+nota2)/2
opc = str(input('Quer mostrar os dados do aluno? ')).upper()[0]
if opc == 'S':
    print(f'Média de {dados["nome"]}: {dados["media"]}')
    if dados['media'] >= 5:
        print(f'Situação é igual a Aprovado')
    elif dados['media'] < 5:
        print(f'Situação é igual a Reprovado')