a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'São apenas espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfanumérico {a.isalnum()}')
print(f'Está em maiúsculo? {a.isupper()}')
print(f'Está em minúsculo? {a.islower()}')
print(f'Está capitalizada? {a.capitalize()}')

