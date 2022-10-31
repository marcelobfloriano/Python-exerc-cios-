soma = 0
impar = 'IMPAR'
par = 'PAR'
totV = 0
print('VAMOS JOGAR PAR OU IMPAR!!')
print('-=' * 13 )
while True:
    numUsu = int(input('Digite um valor: '))
    escUsu = str(input('Par ou Impar[P/I]: ')).upper().strip()[0]
    print('-' * 50)
    from random import randint
    numCpu = randint(1, 20)
    soma = numUsu + numCpu
    if soma % 2 == 0:
        r = par
    elif soma % 2 == 1:
        r = impar
    print(f'Voce jogou {numUsu} cpu {numCpu}. Total de {soma} DEU {r}')
    if escUsu == 'P' and r == par:
        totV += 1
        print('-' * 50)
        print(f"VOCE VENCEU!!!")
        print('Vamos jogar novamente...')
    elif escUsu == 'I' and r == impar:
        totV += 1
        print('-' * 50)
        print(f"VOCE VENCEU!!!")
        print('Vamos jogar novamente...')
    elif escUsu == 'P' and r == impar:
        print('-' * 50)
        print(f"VOCE PERDEU!!!GAME OVER!!!")
        print(f'Voce venceu {totV} vezes')
        break
    elif escUsu == 'I' and r == par:
        print('-' * 50)
        print(f"VOCE PERDEU!!!GAME OVER!!!")
        print(f'Voce venceu {totV} vezes')
        break