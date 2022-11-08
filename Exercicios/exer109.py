import moedas

num = float(input('Digite o preço: R$ '))

print(f'Acrescimo de 10% -> {moedas.aumentar(num, True)}')
print(f'Diminuindo 10% -> {moedas.diminuir(num, True)}')
print(f'O dobro -> {moedas.dobro(num, True)}')
print(f'Metade do valor -> {moedas.metade(num)}')