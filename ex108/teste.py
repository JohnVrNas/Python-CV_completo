import os
os.system('cls')
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentando(p, 10))}')
print(f'Reduzindo 13%, temos R${moeda.moeda(moeda.diminuindo(p, 13))}')