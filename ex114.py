import urllib.request

# URL do site que você quer acessar
url = 'http://www.pudim.com.br'

try:
    conexao = urllib.request.urlopen(url)
except:
    print('O site não está acessível neste momento')
else:
    print('Consegui acesar o site pudim com sucesso')





