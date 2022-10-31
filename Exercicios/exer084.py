temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Digite o nome: ")))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
            break
print('=-' * 30)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {maior} KG. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menor} KG. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
