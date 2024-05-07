from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for m in range(1, 8):
    ano = int(input(f'Em que ano a {m}º pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
