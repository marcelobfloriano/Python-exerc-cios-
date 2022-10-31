vPag = float(input("Digite o valor a ser pago: R$ "))
print('''Escolha a forma de pagamento 
[1] – à vista dinheiro/cheque
[2] - 1x no cartão  
[3] - no cartao parcelado''')

fPag = int(input())

if fPag == 1:
    vPag = vPag - ((vPag * 10) / 100)
    print("Valor do pagamento a vista: R$ {}".format(vPag))
if fPag == 2:
    vPag = vPag - ((vPag * 5) / 100)
    print("Valor do pagamento 1x no cartao: R$ {}".format(vPag))
if fPag == 3:
    vezes = int(input("Em quantas vezes?:"))
    if vezes <= 2:
        print("Serao {} parcelas de {:.2f}".format(vezes, (vPag / vezes)), end='')
        print(" Valor total de {:.2f}".format(vPag))
    elif vezes > 2:
        vPag = vPag + ((vPag * 20) / 100)
        print("Serao {} parcelas de R$ {:.2f}".format(vezes, (vPag / vezes)), end='')
        print("  Valor total de R$ {:.2f}".format(vPag))
