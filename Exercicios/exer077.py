cores = ("amarelo", "preto", "azul",
            "branco", "roxo", "laranja",
            "cinza", "lilas", "abobora")
for pos in cores:
    print(f'\nNa palavra {pos.upper()} temos as vogais: ', end='')
    for letra in pos:
        if letra.lower() in "aeiou":
            print(letra, end= ' ')
