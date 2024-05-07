frase = str(input('Digite uma frase para saber se ela é um \033[34mPalíndromo\033[m: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for pali in range(len(junto)-1, -1, -1):
    inverso += junto[pali]
print(f'O inverso de {frase} é {inverso}')
if inverso == junto:
    print('Achamos um palíndromo!!')
else:
    print('Esta frase não é um palíndromo')

