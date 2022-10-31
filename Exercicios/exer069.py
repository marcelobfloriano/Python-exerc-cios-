continuar = 'S'
pmi = 0
homens = 0
mmv = 0
print('-=' * 10)
while continuar in 'S':
    print('CADASTRO DE PESSOAS')
    print('-=' * 10)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo?[M/F]: ')).upper().strip()[0]
    if idade > 18:
        pmi += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mmv += 1
    print('-=' * 10)
    continuar = str(input(f'Deseja continuar?[S/N]: ')).upper().strip()[0]
print('-=' * 20)
print(f'Total de {pmi} pessoas com mais de 20 anos')
print(f'Total de {homens} homens cadastrados')
print(f'Total de {mmv} mulheres com menos de 20 anos')