from random import choice
print('Um professor tem 5 alunos, e deve sortear qual deles irá apagar o quadro negro. \nSua tarefa é nomear esses alunos')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
n5 = input('Quinto aluno: ')
list = [n1, n2, n3, n4, n5]
win = choice(list)
print('O aluno sorteado foi {}'.format(win))


