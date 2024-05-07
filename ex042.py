print('-=-'*10)
print('Analisador de triângulos')
print('-=-'*10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('É possível formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('NÃO é possìvel formar um triângulo com os segmentos acima')
