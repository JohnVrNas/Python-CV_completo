import os
os.system('cls')

print('-='*15)
def ficha(nome='<desconhecido>', gols = 0):
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')



n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

