def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


def linha():
    print('-'*35)


def resumo(n=0, por_aumento=0, por_diminuindo=0):
    linha()
    print('         RESUMO DO VALOR')
    linha()

    # metade
    
    print(f'Preço analisado:       R${moeda(n)}')

    res = n * 2
    print(f'Dobro do preço:        R${moeda(res)}')

    res = n / 2
    print(f'Metade do preço:       R${moeda(res)}')

    res = n+((n*por_aumento)/100)
    print(f'{por_aumento}% de aumento:        R${moeda(res)}')

    res = n-((n*por_diminuindo)/100) 
    print(f'{por_diminuindo}% de redução:        R${moeda(res)}')
    
    linha()
