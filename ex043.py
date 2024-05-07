print('O índice de massa corporal é uma medida internacional usada \npara calcular se uma pessoa está no peso ideal.')
print('Para saber o seu IMC basta colocar as medidas abaixo')
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}')
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 24.9:
    print(f'Seu IMC é de {imc:.1f}')
    print('Você está em seu PESO NORMAL')
elif 25 <= imc < 29.9:
    print(f'Seu IMC é de {imc:.1f}')
    print('Você está em SOBREPESO')
elif imc > 30:
    print(f'Seu IMC é de {imc:.1f}')
    print('Você está com OBESIDADE')
elif imc > 35:
    print(f'Seu IMC é de {imc:.1f}')
    print('Você está com OBESIDADE EXTREMA! \nTenha cuidado!')

