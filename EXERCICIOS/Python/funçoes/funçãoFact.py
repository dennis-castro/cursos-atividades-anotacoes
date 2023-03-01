def fatorial(n, show=False):
    """
    -> Calcule o fatorial de um numero
    :param n:O numero a ser calculado
    :param show:(opcional) Mostrar ou não a conta
    :return:O valor fatorial de  um numero 'n'
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
print(fatorial(7, show=True))
