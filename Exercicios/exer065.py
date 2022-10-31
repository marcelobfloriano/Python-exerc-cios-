soma = menor = maior = total = 0
resp = 'S'
while resp in 'Ss':
    nume = int(input('Digite um numero: '))
    soma += nume
    total += 1
    if total ==1:
        maior = menor = nume
    elif nume > maior:
        maior = nume
    elif nume < menor:
        menor = nume
    resp = str(input('Quer continuar[S/N]:')).upper().strip()[0]
media = soma / total
print('Voce digitou {} vezes. A media entre eles {}'.format(total, media))
print('O maior valor {}, menor valor {}'.format(maior, menor))