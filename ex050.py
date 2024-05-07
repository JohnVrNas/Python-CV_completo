from time import sleep
s = 0
for r in range(1, 7):
    n = int(input(f'Digite o {r} número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma dentre os números dados que são pares é de {s}')
if 0 != n % 2:
    print('Não foi possível completar a soma')
    sleep(1)
    print('Por favor, tente com outros números')






