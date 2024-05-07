print('-=-'*15)
print('Analisador de triângulos')
print('-=-'*15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('É possível formar um triângulo com os segmentos acima')
else:
    print('NÃO é possìvel formar um triângulo com os segmentos acima')

