t = int(input('Digite um número para saber sua tábuada: '))
print('-' * 10, f'TÁBUADA DO {t}', '-' * 10)
for tabuada in range(1, 11):
    print('-' * 12)
    print(f'{t} x {tabuada:2} = {t*tabuada}')
    print('-'*12)
