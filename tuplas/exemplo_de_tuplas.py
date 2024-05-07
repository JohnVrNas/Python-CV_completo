import os
os.system('cls')
# Isso ai em baixo é uma tupla
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('-'*20)
# vai mostrar o que está na posição 1
print(lanche[1])
print('-'*20)
#vai mostrar o lanche na posição 2 ao contrário, do final até o início
print(lanche[-2])
print('-'*20)
# escrever da posição 1 até a 2, pois o último número é ignorado
print(lanche[1:3])
print('-'*20)
# vai escrever do 0 até o 1
print(lanche[:2])
print('-'*20)
