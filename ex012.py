import time
print('Bem vindo à nossa loja! Sabia que todos os nossos produtos estão com desconto de 5%? \nÉ só colocar o preço abaixo e aparecerá o novo valor!')
time.sleep(2)
number = float(input('Coloque o preço original aqui: R$'))
time.sleep(1.75)
print('Calculando...')
time.sleep(1.75)
d = number*5/100
d2 = number - d
print('Aqui está! \nO valor de sua compra ficou R${:.2f}'.format(d2),'\nAgradecemos sua compra!')

