import time
time.sleep(1)
print("""Olá, sua hora de viajar chegou!
Para saber o valor de sua passagem 
é só digitar a distância entre o local
de partida e o destino final!""")
time.sleep(4)
dis = float(input('Digite a distância aqui: '))
valor = dis*0.50
valor2 = dis*0.45
time.sleep(1)
print('Calculando...')
time.sleep(1)
if dis <= 200:
    print('-'*25)
    print('O valor da passagem ficou R${} \n'
          'Viu como ficou mais fácil?!'.format(valor))
    print('-'*25)
else:
    print('-'*25)
    print('O valor da passagem ficou R${} \n'
          'Viu como ficou mais fácil?!'.format(valor2))
    print('-'*25)
