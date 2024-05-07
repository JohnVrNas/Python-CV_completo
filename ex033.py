pri = int(input('Primeiro valor: '))
segu = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))
menor = pri
if segu<pri and segu<ter:
    menor = segu
if ter<pri and ter<segu:
    menor = ter
    maior = pri
if segu>pri and segu>ter:
    maior = segu
if ter>pri and ter>segu:
    maior = ter
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))


