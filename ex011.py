import time
print('Você quer pintar sua parede mas não sabe os cálculos necessários? Relaxa, eu te ajudo!')
time.sleep(2)
print('Primeiro, preciso saber de algumas medidas da sua parede, apenas em números ok?!')
time.sleep(1.75)
number1 = float(input('Qual é a altura da sua parede?; '))
time.sleep(1.25)
print('Ok! Quase lá...')
number2 = float(input('Qual é a largura da sua parede?; '))
time.sleep(1.75)
print('Carregando...')
time.sleep(2)
m = number1 * number2
time.sleep(1.25)
print('Tá na mão chefia! Sua parede tem {} metros cúbicos!'.format(m))
time.sleep(1.5)
t = m/2
print('Ahh... Quase ia me esquecendo \nEu calculei também quantas latas de tinta vai precisar!')
time.sleep(1.25)
print('Você vai precsiar de {} latas para pintar sua parede de {} m'.format(t, m))
time.sleep(1.5)
print('Espero que tenha ajudado!')









