import os
os.system('cls')


def fatorial(num, show=False):
    """fatorial(n, show=False)
    -> Calcula o fatorial de um número
    Args:
        num (_int_): O número a ser calculado
        show (bool, optional): Mostras ou não a conta. Defaults to False.

    Returns:
        O valor do fatorial de um número n.
    """

    print('-='*13)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(c, end=' X ')
    return f



print(fatorial(5, show = False))