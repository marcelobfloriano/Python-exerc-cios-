jogador = {}
partidas = []
jogador['nome'] = str(input("Nome: "))
num = int(input("Numero de partidas: "))
jogador['gols'] = 0
jogador['total'] = 0
for i in range(0, num):
    partidas.append(int(input(f"Gols na partida {i}: ")))
    jogador['total'] += partidas[i] 
jogador['gols'] = partidas
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f' O jogador {jogador["nome"]} jogou {num} partidas')
for c in range(0, len(partidas)):
    print(f'    =>Na partida {c}, fez {partidas[c]} gols')