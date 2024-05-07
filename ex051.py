print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)
number = int(input('O número: '))
raz = int(int(input('Razão: ')))
decimo = number + (10-1) * raz
for pa in range (number, decimo+raz, raz):
    print(pa, end=' -> ')
print('...')


