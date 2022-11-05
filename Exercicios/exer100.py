from random import randint
from time import sleep
def sorteia():
    a = []
    for c in range(0,5):
        a.append(randint(1,10))
    print(f'Sorteando {len(a)} valores da lista:', end=' ')
    for c in range(0, len(a)):
        print(f'{a[c]}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    return a

def somaPar(a):
    soma = 0
    for c in range(0, len(a)):
        if a[c] % 2 == 0:
            soma += a[c]
    print(f'Somando os valores pares de {a}, temos: {soma}')


l = sorteia()
somaPar(l)