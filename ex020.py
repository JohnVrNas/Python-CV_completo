from random import shuffle
print('Ordem de apresentação do trabalho')
print('-'*12)
std1 = str(input('Primeiro aluno: '))
std2 = str(input('Segundo nome: '))
std3 = str(input('Terceiro nome: '))
std4 = str(input('Quarto nome: '))
list = [std1, std2, std3, std4]
order = shuffle(list)
print('A ordem ficou {}'.format(list))
