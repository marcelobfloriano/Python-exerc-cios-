lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar(S/N)?: ')).upper().strip()[0]
    if continuar == 'N':
        break
if 5 in lista:
    print('O numero 5 foi digitado e esta na lista')
else:
    print('O numero 5 nao foi digitado')
print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(lista)
