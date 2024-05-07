from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de lista conteúdo do arquivo
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(0.5)