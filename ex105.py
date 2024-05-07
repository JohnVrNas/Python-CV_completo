import os
os.system('cls')

def notas(*num, sit=False):
    """
    notas(*n, sit=False)
        -> Função para analisar notas e situações de vários alunos.
        :param n: Uma ou mais notas e situações de vários alunos;
        :param sit: Valor opcional, indicado se deve ou não adicionar a situação
        :return: Dicionário com várias informações sobre a situação da turma
    """
    dicio = {}
    dicio['total'] = len(num)
    dicio['media'] = sum(num) / len(num)
    dicio['maior'] = max(num)
    dicio['menor'] = min(num)
    if sit:
        if dicio['media'] >= 7:
            situacao = 'Boa'
        elif dicio['media'] >= 5 and dicio['media'] < 7:  # Corrigido
            situacao = 'Razoável'
        else:
            situacao = 'Ruim'
        dicio['situacao'] = situacao  # Adicionando a situação ao dicionário
    return dicio

resultados = notas(3.5, 2.5, 5, 6.5, 10, 5.7, 2.5, sit=True)  # Adicionando sit=True para obter a situação
print(resultados)