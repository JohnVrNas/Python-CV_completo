import os
os.system('cls')
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentando(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuindo(p, 13)}')