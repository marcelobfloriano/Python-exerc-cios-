sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos!! Informe Qual seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
elif sexo == 'F':
    sexo ='FEMININO'
print('Sexo {} registrado com sucesso'.format(sexo))