from datetime import datetime
pessoas = {}
pessoas['nome'] = str(input("Nome: ")).upper()
pessoas['idade'] = int(input("Ano do Nascimento: "))
pessoas['ctps'] = int(input("Carteira de Trabalho(0 nao tem): "))
pessoas['idade'] = datetime.now().year - pessoas['idade'] 
if pessoas['ctps'] == 0:
    for k, v in pessoas.items():
        print(f'{k} tem o valor {v}')
else:
    pessoas['anodecontrataçao'] = int(input("Ano de Contratação: "))
    pessoas['salario'] = float(input("Salario: R$ "))
    pessoas['aposentadoria'] = (35 + pessoas['idade']) - (datetime.now().year - pessoas['anodecontrataçao']) 
    for k, v in pessoas.items():
        print(f'{k} tem o valor {v}')