def notas(*num, sit=False):
    notasAlunos = {}
    maior = menor = media = soma = 0
    notasAlunos['total'] = len(num)
    for c in range(0, len(num)):
        if c == 0:
            maior = menor = num[c]
        if num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
        soma += num[c]
    media = soma / len(num)
    notasAlunos['maior'] = maior
    notasAlunos['menor'] = menor
    notasAlunos['media'] = media
    if sit == True:
        if media < 5:
            notasAlunos['situação'] = 'RUIM'
        elif media >= 5 and media < 8:
           notasAlunos['situação'] = 'BOM' 
        elif media >= 8 and media <= 10:
            notasAlunos['situação'] = 'OTIMO'
    return notasAlunos


r = notas(8, 10, 8, 8.5, sit=True)
print(r)