import os
os.system('cls')
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
numeros = (5,7,9,3,4,6,2,1)
# maneira funcional e prática, mas não mostra a posição da informação
for c in lanche:
    print(f'Eu vou comer {c}')
print('-'*30)
# faz a mesma coisa, mas tem um contador que possibilita mostrar a posição da informação
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-'*30)
# jeito fácil de mostrar a posição, usando o enumerate
for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
resp = ' '
while resp not in 'SN':
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'S':
        # ordena a lista em ordem alfabética
        print(sorted(lanche))
        # e em ordem crescente 
        print(sorted(numeros))
