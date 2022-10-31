from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
print('-=' *18)
print('         JOGOS DA MEGA            ')
print('-=' *18)
quantidade = int(input('Quantos jogos quer fazer? '))
while tot <= quantidade:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 4, f'SORTEANDO {quantidade} JOGOS', '-=' * 4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-' * 4, f'BOA SORTE', '-=' * 4)