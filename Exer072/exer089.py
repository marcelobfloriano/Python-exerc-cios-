temp = []
alunos = []
parar = 0
while True:
    temp.append(str(input("Digite o nome: ")).upper())
    temp.append(float(input("Digite a nota 1: ")))
    temp.append(float(input("Digite a nota 2: ")))
    alunos.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-' * 14)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>10}')
print('-' * 28)
for i, l in enumerate(alunos):
    print(f'{i:<4}{l[0]:<10}{(l[1] + l[2]) / 2:>8.1f}')
while True:
    parar = int(input("Quer a nota de qual aluno?[999]para sair: "))
    if parar == 999:
        break
    if parar >= len(alunos) and parar != 999:
        print('Aluno invalido!!!')
    else:
        print(f'Notas de {alunos[parar][0]} -> {alunos[parar][1]} e {alunos[parar][2]}')

