print('='*10, 'GERADOR DE PA', '='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('Fim')