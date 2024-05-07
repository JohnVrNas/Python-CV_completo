import os
os.system('cls')
a = (2,5,4)
b = (5,8,1,2)
# juntando tuplas
c = b+a
print(c)
print('-'*20)
# mostra quantas vezes um número apareceu na tupla
print(c.count(5))
print('-'*20)
# mostra a posição do número definido
print(c.index(2))
print('-'*20)
# o segundo número determina onde a contagem será iniciada
print(c.index(2, 4))
print('-'*20)
pessoa = ('João', 18, 'M', 80)