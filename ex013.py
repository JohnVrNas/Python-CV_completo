import time
print('Meus parabéns! Se você está aqui quer dizer que recebeu um aumento!')
time.sleep(1.75)
a = float(input('Para saber quanto irá ganhar no próximo pagamento, coloque o seu salário atual aqui;R$'))
p = a*15/100
p1 = p+a
time.sleep(1.25)
print('Calculando')
time.sleep(1.25)
print('Você começara à receber R${} já no próximo pagamento'.format(p1))