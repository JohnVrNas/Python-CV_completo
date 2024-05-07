#valores acima de 1250 10%. Para inferiores ou iguais 15%
salario = float(input('Qual é o salário do funcionário? R$'))
if salario<=1250.00:
    print('O salário de R${}, agora passara a ser de R${}'.format(salario, ((salario*15)/100+salario)))
if salario>1250.00:
    print('O salário de R${}, agora passara a ser de R${}'.format(salario, ((salario*10)/100+salario)))



