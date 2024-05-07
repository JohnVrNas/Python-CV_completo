n= cont = s = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números e a soma entre eles foi de {s}')


