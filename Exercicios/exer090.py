alunos = {}
alunos['nome'] = str(input('Nome do aluno: ')).upper()
alunos['media'] = float(input('Media do aluno: '))
if alunos['media'] < 7.5 and alunos['media'] >= 5:
    alunos['situaçao'] = 'RECUPERAÇAO'
elif alunos['media'] < 5:
    alunos['situaçao'] = 'REPROVADO'
elif alunos['media'] >= 7.5 and alunos['media'] <= 10:
    alunos['situaçao'] = 'APROVADO'
print('-=' * 20)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')  
    