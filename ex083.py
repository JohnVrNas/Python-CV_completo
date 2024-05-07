import os
os.system('cls')
expressao = str(input('Digite a expressão: '))
parenteses_abertos = []
parenteses_fechando = []
for i in expressao:
    if i == '(':
        parenteses_abertos.append('(')
    elif i == ')':
        parenteses_fechando.append(')')
if parenteses_abertos.count('(') == parenteses_fechando.count(')'):
    print('Operação válida')
else:
    print('Operação inválida')