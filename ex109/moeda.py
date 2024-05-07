def metade(n = 0, formato = False):

    res = n / 2
    return res if formato is False else moeda(res)
    

def dobro(n = 0, formato = False):

    res = n * 2
    return res if formato is False else moeda(res)


def aumentando(n = 0, por_aumento = 0, formato = False):

    res = n+((n*por_aumento)/100)
    return res if formato is False else moeda(res)


def diminuindo(n = 0, por_diminuindo = 0, formato=False ):

    res = n-((n*por_diminuindo)/100) 
    return res if formato is False else moeda(res)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


