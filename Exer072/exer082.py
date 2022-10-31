listapar = []
listaimpar = []
lista = []
n = 0
while True:
    n = (int(input('Digite um numero: ')))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 == 1:
        listaimpar.append(n)
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Lista completa {lista}')
print(f'Lista de pares {listapar}')
print(f'Lista de impares {listaimpar}')