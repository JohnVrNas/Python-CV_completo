import os
os.system('cls')
def area(larg, compr):
   
    soma = compr*larg
    print(f'A área de um terreno {larg} X {compr} é de {soma:.1f}m²')


print('Controle de Terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg, compr)