valores = []
while True:
    n = (int(input(f'Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Registro efetuado com sucesso!!!')
    else:
        print('Valor duplicado. Nao vou adicionar!!!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar(S/N)?: ')).upper().strip()[0]
    if continuar == 'N':
        break
valores.sort()
print(f'Voce digitou os valores {valores}')
