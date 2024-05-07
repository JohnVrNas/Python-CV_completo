import os
from ex111.utilidadesCev import moeda
from ex112.utilidadesCev import dados
os.system('cls')


p = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
