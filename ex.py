from time import sleep
renda = dep = ''
print('Calculadora de Imposto de Renda')
print('-'*31)
#leitura de dados
name = str(input('Digite seu nome completo: ')).strip()
partes = name.split()
primeironome = partes[0]
print(f'Olá {primeironome}! Bem-Vindo a Receita Federal!')
sleep(1)
print('Coloque suas informações abaixo por gentileza')
sleep(1)
print('-'*31)
sleep(2)
csp = float(input('Digite seu CPF: '))
sleep(1)
while True:
    renda = int(input('Digite sua renda mensal: R$'))
    if renda < 0:
        sleep(1)
        print('Valor inválido...Tente novamente')
        sleep(2)
    else:
        break
sleep(1)
while True:
    resp = str(input('Você tem dependentes? [S/N]: ')).strip().upper()[0]
    if resp == 'S':
        dep = int(input('Quantos dependentes você tem? '))
        if dep < 0:
            sleep(1)
            print('Valor inválido...Tente novamente')
            sleep(2)
        else:
            break
    elif resp not in 'NS':
        print('Resposta Inválida...Tente novamente')
    else:
        dep = 0
        break
rendanual = renda*12
#desconto por dependente
descon = (dep * 110)
#salário líquido
liq = rendanual-descon
sleep(1)
print('Calculando...')
sleep(3)
if liq < 800:
    print('Você é isento de imposto')
else:
    if liq >= 800 and liq <= 4000:
        imp = (liq*2.5)/100
    if liq >=4001 and liq <=9000:
        imp = (liq*5)/100
    if liq > 9000:
        imp = (liq*10)/100
print('='*31)
print(f'O total da sua renda anual é de R${rendanual}')
print(f'O desconto que você tem por dependente é de R${descon} em cima do seu salário anual')
print(f'O valor do imposto a pagar é de R${imp:.2f}')
