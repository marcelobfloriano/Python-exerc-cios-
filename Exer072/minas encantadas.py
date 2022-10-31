
matriz1 = [[42, -1, 90, 40, -9, -47, 99, -59, -52, -21, -39, -62, 1, 63, 21, 0, -84, -95, 46, 49],
          [94, 86, 62, 86, 64, 71, -38, -21, 10, -75, 66, -66, 52, 45, 70, -57, 86, 38, 40, 84],
          [37, -26, -91, -30, 26, -11, -45, 92, 36, 75, 26, -62, -79, -94, 72, -99, 74, 31, -84, -11],
          [21, 24, 88, 30, -70, -80, 61, -47, 6, 5, 46, 94, -27, 35, 73, -26, -62, 60, -40, -24],
          [-18, -72, 78, 72, 59, 21, 7, -28, -57, 6, 85, -5, 21, -13, 21, -26, -81, 90, -66, -79],
          [60, 0, -15, -77, -2, 7, 78, 4, 94, -50, -58, 78, 53, -21, 18, 39, 46, 18, 20, -6],
          [-74, -58, 32, -47, 78, 66, -3, 27, 48, 9, 62, -32, 73, 20, 14, 88, 24, -3, 72, -89],
          [72, -67, 10, 92, -80, 98, 70, 30, -49, 58, -70, -26, 80, 66, -39, 83, -29, 92, -33, -14],
          [-23, 12, 34, -6, 95, -20, 4, -98, 10, -12, 92, 87, -63, -21, -42, -89, -9, -91, 49, -5],
          [-86, 35, -70, -44, -1, -68, -15, -36, -70, 28, -44, -96, 13, -25, 44, 18, -62, 53, 41, -35],
          [63, 36, 47, 19, 52, -38, -46, -25, -27, -56, 74, -75, 84, -86, -12, -31, -65, -3, -20, 52],
          [45, -88, -1, 76, -11, -77, 18, 14, 95, -1, 1, -89, -1, -8, -21, 17, 96, -46, -34, 57],
          [67, 16, -88, -73, 62, 93, -51, 49, 81, -34, 31, 61, -10, 46, 50, -36, 39, -16, -98, -60],
          [93, 35, -99, 65, 1, -52, 68, 20, 83, -62, 13, 86, -69, -94, -69, -85, -70, 19, 88, -77],
          [21, -98, 54, -1, 11, -90, 87, -24, 0, -81, 33, 28, -72, 29, 41, -59, 34, -86, 31, 28],
          [83, -51, -93, 74, -9, 3, 31, -6, -13, 36, -15, -34, 33, -36, -74, 16, -37, -87, -23, -83],
          [1, 3, 44, 37, -27, -26, -61, 41, 89, 57, -22, -38, 0, -87, -100, -68, -62, -30, -14, 16],
          [-65, -76, -52, 69, 71, 25, -76, 36, 46, 33, -90, 10, 30, -37, 92, -80, 50, -9, 33, -33],
          [-19, -87, 41, 25, 75, 82, 57, -51, 53, -16, 78, -35, -98, -12, 55, -12, 53, 80, -3, 60],
           [74, -48, -30, 71, -25, -80, 57, -69, 6, 46, -13, -24, -66, 13, 75, -24, -11, -10, 22, 61]]

def calculomaiorlucro(matriz, retlargura, retaltura):
    lucros = []
    alturamaiorvalor = 0
    larguramaiorvalor = 0
    maiorlucro = 0
    for e in range(0, len(matriz)-1):
        if len(matriz) > e and len(matriz[e]) != len(matriz[e+1]):
            raise Exception('Matriz esta inconsistente')
    for m in range(0, len(matriz)):
        for n in range(0, len(matriz[0])):
            lucros.append(calcularlucropelopontocartesiano(matriz, n, m, retlargura, retaltura))
    '''for i in range(0, len(lucros)):
        for z range(0, len(lucros[0]))'''


def calcularlucropelopontocartesiano(matriz, pilargura, pialtura, largura, altura):
    soma = 0
    if largura < 1 or altura < 1:
        raise Exception('Altura e Largura deve ser maior que 0')
    elif not((largura == (2 * altura)) or (altura == (2 * largura))):
        raise Exception('Isso nao e um retangulo')
    elif not matriz:
        raise Exception('A Matriz esta vazia')
    elif len(matriz[0]) < largura + pilargura:
        raise Exception('Largura maior que o terreno')
    elif len(matriz) < altura + pialtura:
        raise Exception('Altura maior que o terreno')
    for e in range(0, len(matriz)-1):
        if len(matriz) > e and len(matriz[e]) != len(matriz[e+1]):
            raise Exception('Matriz esta inconsistente')
    for m in range(pialtura, pialtura + altura):
        for n in range(pilargura, pilargura + largura):
            soma += matriz[m][n]
    return soma



try:
    ret = calcularlucropelopontocartesiano(matriz1, 0, 0, 1, 2)
    print(ret)
except Exception as m:
    print(m)












'''somamaior = opcao = opcaomaior = soma = 0

def calculaarea(a, b, c, d):
    soma = 0
    for m in range(a, b):
        for n in range(c, d):
            soma += matriz[m][n]
    
    print(soma)
    return soma

calculaarea(0,2,0,4)
print(soma)'''


'''for m in range(0, 2):
    for n in range(0, 4):
        soma += matriz[m][n]
        print(matriz[m][n], end=' -> ')
        print(f'm: {m} n: {n}', end='  ')


print(f'Soma Atual:{soma}')

opcao += 1
soma = 0
''for m in range(a, b):
    for n in range(c+4, d+4):
        soma += matriz[m][n]
        print(matriz[m][n], end=' -> ')
        print(f'm: {m} n: {n}', end='  ')
        if soma > somamaior:
            somamaior = soma
            opcaomaior = opcao
print(f'\nOpcao atual:{opcao}')
print(f'Soma Atual:{soma}')
print(f'Opcao maior:{opcaomaior}')
print(f'Soma maior:{somamaior}')'''''


