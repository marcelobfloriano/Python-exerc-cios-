import moedas

num = float(input('Digite o preço: R$ '))

print(f'Acrescimo de 10% -> {moedas.moeda(moedas.aumentar(num))}')
print(f'Diminuindo 10% -> {moedas.moeda(moedas.diminuir(num))}')
print(f'O dobro -> {moedas.moeda(moedas.dobro(num))}')
print(f'Metade do valor -> {moedas.moeda(moedas.metade(num))}')