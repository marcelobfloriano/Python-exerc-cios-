def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n = str(input('Nome do jogador: ')).upper()
g = str(input('Qtd de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = '<desconhecido>'
ficha(n, g)
