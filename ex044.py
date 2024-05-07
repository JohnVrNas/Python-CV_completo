import time
print('='*10, 'LOJA DO JOCA', '=' *10)
compras = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO 
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão""")
option = int(input('Qual é a opção? '))
if option == 1:
    print(f'A compra de R${compras:.3f} vai custar R${compras-(compras*10/100):.3f} com desconto de 10%')
elif option == 2:
    print(f'À vista no cartão a compra de R${compras:.3f} vai custar R${compras - (compras*5/100):.3f} com desconto de 5%')
elif option == 3:
    print(f'2x no cartão de crédito o valor da compra fica R${compras:.3f}')
elif option ==4:
    print(f'3x ou mais no cartão a compra de R${compras:.3f} vai custar R${compras+(compras*20/100):.3f}')
time.sleep(1.5)
hour = time.strftime('H.%M', time.localtime())
if hour >= '05:00' and hour <='12:00':
    print('Tenha um Bom Dia!')
elif hour > '12:00' and hour <= '17:59':
    print('Tenha uma Boa Tarde !')
else:
    print('Tenha uma Boa Noite!')



