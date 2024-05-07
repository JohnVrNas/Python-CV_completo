def metade(n = 0):
    res = n / 2
    return res
def dobro(n = 0):
    res = n * 2
    return res

def aumentando(n = 0, por_aumento = 0):
    res = n+((n*por_aumento)/100)
    return res

def diminuindo(n = 0, por_diminuindo = 0 ):
    res = n-((n*por_diminuindo)/100) 
    return res

def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')