salario = float(input('Qual é o seu salário atual? R$'))
casa = float(input('Qual é o valor da casa? R$'))
anos = int(input('Em quantos anos o valor será financiado? '))
final = casa / (anos * 12)
porcento = salario * 30/100
print(f'Para comprar uma casa de R${casa} em {anos} anos a mensalidade será de R${final:.3f}')
if porcento > final:
    print('O Empréstimo \033[32mPODERÁ\033[m ser contratado!')
else:
    print('O Empréstimo \033[31mNÃO\033[m poderá ser contratado')