totIdade = 0
nomeHMV = ''
idadeHMV = 0
mulherMVA = 0
for c in range(0, 4):
    nome = input('Nome da {}ª pessoa: '.format(c +1))
    idade = int(input('Idade: '))
    sexo = input("SEXO(M/F): ")
    totIdade += idade
    if idade > idadeHMV:
        idadeHMV = idade
        nomeHMV = nome
    if sexo == 'f' and idade < 20:
        mulherMVA += 1
print('A media de idade é {}'.format(totIdade / 4))
print('Com {} anos {} é homem mais velho'.format(idadeHMV, nomeHMV))
print('{} mulheres têm menos de 20 anos'.format(mulherMVA))
