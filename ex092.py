import datetime
import os
os.system('cls')

dados = {}
dados['nome'] = str(input('Digite seu nome completo: ')).strip()
ano = int(input('Digite o seu ano de nascimento: '))
dados['idade'] = datetime.datetime.now().year - ano
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Digite o ano da contratação: '))
    dados['salario'] = float(input('Digite seu salário: R$'))
    dados['aposentadoria'] = dados['idade']+ ((dados['contrato'] + 35) - datetime.datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
