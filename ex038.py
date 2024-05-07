number = float(input('Primeiro valor: '))
number2 = float(input('Segundo valor: '))
if number > number2:
    print(f'O valor {number} é MAIOR que o valor {number2}')
elif number < number2:
    print(f'O valor {number} é MENOR que o valor {number2}')
else:
    print('Os valores são IGUAIS')
