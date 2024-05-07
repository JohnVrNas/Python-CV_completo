from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo para saber seu sen, coss e tan: '))
rad = radians(ang)
sen = sin(rad)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
coss = cos(rad)
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
tan = tan(rad)
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))


