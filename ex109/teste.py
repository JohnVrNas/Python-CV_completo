import os
os.system('cls')
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentando(p, 10, True)}')
print(f'Reduzindo 13%, temos R${moeda.diminuindo(p, 13, True)}')