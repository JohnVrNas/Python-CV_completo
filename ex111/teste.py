import os
from ex111.utilidadesCev import moeda
os.system('cls')


p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)