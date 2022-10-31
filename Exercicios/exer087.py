sompar = somtercol = msl = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f"Digite um numero{[l, c]}: ")))
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
        if c == 2:
            somtercol += matriz[l][c]
        if l == 1:
            if matriz[1][c] > msl:
                msl = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os pares é: {sompar}')
print(f'A soma da terceira coluna é: {somtercol}')
print(f'O maior numero da segunda linha é: {msl}')