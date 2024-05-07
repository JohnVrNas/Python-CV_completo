resp = 'S'
soma = cont = med = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
med = soma / cont
print(f'Você digitou {cont} números e a média entre eles foi de {med}')
print(f'O maior número digitado foi  {maior} e o menor foi {menor}')
