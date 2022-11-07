def fatorial(fatorial, show):
    """
    Calcula o fatorial de um numero
    fatorial = numero que vai calcular o fatorial
    show = mostrar os nao a conta
    return = valor do calculo do fatorial
    """
    fat = 1
    if show == True:
        for c in range(fatorial, 0, -1):
            print(f'{c}', end=' ')
            if c > 1:
                print(f' X ', end=' ')
            else:
                print(f' = ', end=' ')
            fat *= c
        return fat
    else:
        for c in range(fatorial, 0, -1):
            fat *= c
        return fat



print(fatorial(5, show=True))
help(fatorial)