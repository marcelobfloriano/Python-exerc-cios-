jogador = {}
golspartidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome: "))
    golspartidas.clear()
    numpartidas = int(input("Numero de partidas: "))
    for i in range(0, numpartidas):
        golspartidas.append(int(input(f"Gols na partida {i+1}: ")))
    jogador['gols'] = golspartidas[:]
    jogador['total'] = sum(golspartidas)
    time.append(jogador.copy())   
    while True:
        continuar = str(input('Quer continuar[S/N]?: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro!! Digite S ou N')
    if continuar == 'N':
        break 
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-' * 30)
for k, v in enumerate(time):
    print(f' {k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='') 
    print()
print('=-' * 30)
while True:
    cont = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if cont == 999:
        break
    if cont >= len(time):
        print(f'Erro!! Nao existe jogador com o codigo{cont}')
    else:
        print(f' Dados do jogador {time[cont]["nome"]} ')
        for i, g in enumerate(time[cont]["gols"]):
            print(f' No jogo {i+1} fez {g} gols')
        print('=-' * 30)
print('VOLTE SEMPRE')