from exer115.lib.interface import *
from exer115.lib.arquivo import *
from time import sleep

arq = 'dadosdeentrada.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('SAINDO do Sistema... Ate logo!')
        break
    else:
        ('ERRO! Digite uma opção valida!!')
    sleep(2)