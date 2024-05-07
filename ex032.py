from datetime import date
ano = int(input('Qual será o ano a ser analisado como BISSEXTO? \nCaso queira analisar o ano atual, basta coloca 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))

