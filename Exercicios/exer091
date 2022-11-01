from random import randint
from time import sleep
from operator import itemgetter
ordem = dict()
jogos = {'jogador1': randint(1,6),
'jogador2': randint(1,6),
'jogador3': randint(1,6),
'jogador4': randint(1,6),}
for k, v in jogos.items():
    print(f'{k} tirou {v}')
    sleep(1)
ordem = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(f'====RANKING DOS JOGADORES====')
print('-=' * 15)
for i,v in enumerate(ordem):
    print(f'{i+1}o lugar: {v[0]} tirou {v[1]}')
    sleep(1)
print(f'{ordem[0][0]} com {ordem[0][1]} foi o VENCEDOR!!! ')