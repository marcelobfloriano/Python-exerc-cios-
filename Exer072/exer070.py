total = pmdm = pmb = cont = 0
nomeBarato = ''
while True:
    nome = str(input('Nome do produto: ')).upper()
    preco = float(input('Preço: R$ '))
    cont += 1
    if cont == 1:
        pmb = preco
        nomeBarato = nome
    total += preco
    if preco > 1000:
        pmdm += 1
    elif preco < pmb:
        pmb = preco
        nomeBarato = nome
    print('-=' * 14)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input(f'Deseja continuar?[S/N]: ')).upper().strip()[0]
    print('-=' * 14)
    if continuar == 'N':
        break
print(f'Total da compra = R$ {total:.2f}')
print(f'{pmdm} produtos custam mais de R$ 1000.00')
print(f'O produto mais barato --> {nomeBarato} custando R$ {pmb:.2f} ')