import moedas

num = float(input('Digite o preço: R$ '))

aumentar = moedas.aumentar(num)
diminuir = moedas.diminuir(num)
dobro = moedas.dobro(num)
metade = moedas.metade(num)
print(f'Acrescimo de 10% -> R$ {aumentar}')
print(f'Diminuindo 10% -> R$ {diminuir}')
print(f'O dobro -> R$ {dobro}')
print(f'Metade do valor -> R$ {metade}')