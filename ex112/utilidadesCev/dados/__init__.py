vermelho = '\033[0;31m'
end = '\033[m'

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(vermelho+f'ERRO: \"{entrada}\" é um preço inválido!'+end)
        else:
            valido = True
            return float(entrada)
