lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print('\t\t\tLISTAGEM DE PREÇOS')
print('-'*40)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:•<30}R$', end = '')
    else:
        print(f'{lista[pos]:8.2f}')
print('-'*40)