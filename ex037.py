n = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[  1  ] BINÁRIO
[  2  ] OCTAL
[  3  ] HEXADECIMAL''')
op = int(input(': '))
if op == 1:
    print(f'O número {n} convertido para binário fica {bin(n)[2:]}')
elif op == 2:
    print(f'O número {n} convertido par octal fica {oct(n)[2:]}')
else:
    print(f'O número {n} convertido para hexadecimal fica {hex(n)[2:]}')
