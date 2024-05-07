from datetime import date
atual = date.today().year
print('\033[0;32m-\033[m''\033[0;30m=\033[m''\033[0;32m-\033[m'*10)
ano = int(input(('Digite o ano de nascimento: ')))
age = atual - ano
if age < 18:
    saldo = 18 - age
    print('\033[0;32m-\033[m''\033[0;30m=\033[m''\033[0;32m-\033[m' * 10)
    print(f"""Você ainda tem {age} anos
Seu alistamento \033[0;32mserá\033[m em \033[0;32m{saldo}\033[m ano(s)""")
    print('\033[0;32m-\033[m''\033[0;30m=\033[m''\033[0;32m-\033[m' * 10)
elif age > 18:
    saldo = age - 18
    print('\033[0;32m-\033[m''\033[0;30m=\033[m''\033[0;32m-\033[m' * 10)
    print(f"""Você tem {age} anos, seu ano de alistamento \033[0;31mjá passou\033[m
Você deveria ter se alistado no ano de {atual - saldo}""")
    print('\033[0;32m-\033[m''\033[0;30m=\033[m''\033[0;32m-\033[m' * 10)
else:
    print('Você completa 18 anos esse ano! \nDeve se alistar' ' \033[0;32mIMEDIA\033[m''\033[0;30mTAMENTE\033[m')