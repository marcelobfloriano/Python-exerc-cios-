pessoa = {}
pessoas = []
media = total = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input(f'Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Digite F ou M! ')
        pessoa['sexo'] = str(input(f'Sexo [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    total += pessoa['idade']
    while True:
        continuar = str(input('Quer continuar[S/N]?: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro!! Digite S ou N')
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
media = total / len(pessoas)
print(f'A media de idade é = {media:5.2f} ')
print(f'As mulheres cadastradas foram ', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista de pessoas acima da media de idade')
for i in pessoas:
    if i['idade'] > media:
        print(f'   Nome = {i["nome"]}, Sexo = {i["sexo"]}, Idade = {i["idade"]}; ')