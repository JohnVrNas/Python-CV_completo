from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    op = int(input('Qual opções você deseja? '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre os valores {n1} e {n2} é de {soma}')
        print('-='*20)
        sleep(2)
    elif op == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é de {mult}')
        print('-='*20)
        sleep(3)
    elif op == 3:
        if n1>n2:
            print(f'O número {n1} é mairo que o {n2}')
            print('-='*20)
        elif n1<n2:
            print(f'O número {n2} é maior que o {n1}')
        elif n1==n2:
            print('O números dados são iguais')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('-='*20)
    elif op == 0 or op > 5:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE...')
print('Ok! A operação será finalizada...')
sleep(1.25)
print('Finalizando...')
sleep(1.25)
print('Volte sempre!')



