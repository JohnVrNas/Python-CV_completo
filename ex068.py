from random import randint
cont = 0
print('=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
v = 0
while True:
    player = int(input('Digite um valor: '))
    comp = randint(0, 11)
    total = player + comp
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {comp}, total de {total}')
    if pi == 'P':
        if total % 2 == 0:
            print('-='*7)
            print('Você venceu!!')
            print('-='*7)
            v += 1
        else:
            print('Você perdeu')
            break
    elif pi == 'I':
        if total % 2 == 1:
            print('-='*7)
            print('Você venceu!!')
            print('-='*7)
            v += 1
        else:
            print('-=' * 7)
            print('Você perdeu')
            print('-=' * 7)
            break
        print('-='*15)
    print('Vamos jogar novamente...?')
print(f'GAME OVER! Você venceu {v} vezes')


