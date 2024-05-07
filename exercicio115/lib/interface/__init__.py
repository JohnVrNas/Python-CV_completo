
global vermelho
vermelho = '\033[91m'

global endcolor
endcolor = '\033[0m'

def leiaint(num):
    while True:
        try:
            num = int(input(num))
        except (ValueError, TypeError):
            print(vermelho+'ERRO: por favor, digite um número inteiro válido.'+endcolor)
            continue
        except KeyboardInterrupt:
            print(vermelho + 'Entrada de dados interrompida pelo usuário.' + endcolor)
            return 0
        else:
            return num


def linha(tam=42):
    return'-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc
