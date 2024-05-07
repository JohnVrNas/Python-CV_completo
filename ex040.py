port = float(input('Digite a nota de Português: '))
mat = float(input('Digite a nota de Matemática: '))
med = (port+mat)/2
if med >= 7:
    print(f'A média do aluno é {med}')
    print('O aluno está \033[0;32mAprovado\033[m!')
elif med < 6 and 7:
    print(f'A média do Aluno é {med}')
    print('O aluno está de \033[0;33mRecuperação\033[m')
else:
    print(f'A média do Aluno é {med}')
    print('O aluno está \033[0;31mReprovado\033[m')

