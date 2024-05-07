print('{:-^40}'.format('LOJA DO SEU TOBA'))
total = totmil = menor = cont = 0
barato = 0
while True:
    name = str(input('Nome de Produto: ')).strip()
    price = int(input('Preço do produto: R$'))
    total += price
    cont += 1
    if price > 1000:
        totmil += 1
    if cont == 1 or price < menor:
        menor = price
        barato = name
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R${total}')
print(f'Temos {totmil} produtos acima de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor}')

