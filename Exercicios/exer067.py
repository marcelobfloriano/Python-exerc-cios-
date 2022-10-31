c = repita = 0
tabuada = 1
while True:
    num = int(input('Qual TABUADA voce quer: '))
    if num < 0:
        break
    repita = 10
    while c < repita:
        c += 1
        tabuada = num * c
        print(f'{c} X {num} = {tabuada}',)
    c = 0
