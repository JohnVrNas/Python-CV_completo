velo = float(input('Qual era a velocidade do carro? '))
multa = (velo-80)*7
if velo > 80:
    print("""MULTADO! Você estava acima do limite de velocidade!
    A multa será de R${}.""".format(multa), '\n Tome mais cuidado da próxima vez!')
print('Tenha um Bom Dia!')


