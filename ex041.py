from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
age = atual - ano
if age <= 9:
    print(f'O atleta tem {age} anos')
    print('Classificação: MIRIM')
elif age <= 14:
    print(f'O atleta tem {age} anos')
    print('Classificação: INFANTIL')
elif age <= 19:
    print(f'O atleta tem {age} anos')
    print('Classificação: JÚNIOR')
elif age == 20:
    print('O atleta tem 20 anos')
    print('Classificação: SÊNIOR')
else:
    print(f'O atleta tem {age} anos')
    print('Classificação: MASTER')

