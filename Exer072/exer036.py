valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do salario: R$"))
tempoPagar = int(input("Em quantos anos quer pagar?:"))
valorParcela = valorCasa / (tempoPagar * 12)
if valorParcela <= (salario * 30) /100:
    print('O valor da parcela é R$ {:.2f} pago em {} anos '.format(valorParcela, tempoPagar))
    print(f'EMPRESTIMO CONCEDIDO!!!')
else:
    print('O valor da parcela é R$ {:.2f} nao pode exceder 30% do salario '.format(valorParcela))
    print(f'EMPRESTIMO NEGADO!!!')