frase = str(input('Digite o seu nome completo: ')).strip()
print('Maiúscula: ', frase.upper())
print('Minúscula: ', frase.lower())
print('Seu nome ao todo tem {} letras'.format(len(frase) - frase.count(' ')))
split = frase.split()
print('Seu primerio nome tem {} letras'.format(len(split[0])))










