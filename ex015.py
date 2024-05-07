days = int(input('Quantos dias o carro foi usado? '))
km = float(input('Quantos KM o carro rodou? '))
import time
time.sleep(1.5)
print('Carregando...')
time.sleep(1.5)
d = 60*days
k = km*0.15
print('O total a pagar é de R${:.2f}'.format(d+k))