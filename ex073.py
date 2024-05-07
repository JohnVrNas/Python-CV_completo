import os
os.system('cls')
times = ('Palmeiras', 'Botafogo', 'Grémio', 'Bragantino', 'Atlético-MG','Flamengo', 'Atlético-PR', 'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 'Goiás','Coritiba', 'América-MG')
print('Esses são os 5 primeiros colocados:')
for pos, c in enumerate(times[0:5]):
    print(f'O {c} está na {pos+1}º posição ')
print('=-'*25)
for pos, c in enumerate(times[-4:]):
    print(f'O {c} está na {pos+17}º posição ')
print('=-'*25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*25)
print(f'O \033[1;31;40mCorinthians\033[m está na {times.index("Corinthians")}º posição ')

