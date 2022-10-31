altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {:.2f}'.format(imc))
    print('IMC abaixo de 18,5, Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Entre 18,5 e 25: Peso Ideal')
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Entre 25 até 30: Sobrepeso')
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Entre 30 até 40: Obesidade')
elif imc >= 40:
    print('Seu IMC é {:.2f}'.format(imc))
    print(' Acima de 40: Obesidade Mórbida')



