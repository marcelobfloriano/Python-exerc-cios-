
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" *30)
listagem = ("caneta", 1.25,
            "lapis", 3.00,
            "borracha", 5,
            "teclado", 20,
            "cadeira", 50,
            "mouse", 25)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
