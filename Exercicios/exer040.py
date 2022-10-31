nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
    print('Com media de {} , O aluno esta REPROVADO!!!'.format(media))
elif 7 > media >= 5:
    print('Com media {} o aluno esta de RECUPERACAO!!!'.format(media))
elif 10 >= media >= 7:
    print('Com media {} o aluno esta APROVADO!!!'.format(media))
else:
    print('Digite uma nota valida(0-10)')


