nove = 0
n = (int(input("Digite um numero:")), int(input("Digite um numero:")),
     int(input("Digite um numero:")), int(input("Digite um numero:")))
print(f'Voce digitou os valores{n}')
print(f'O numero 9 aparece {n.count(9)} vezes')
if 3 in n:
     print(f'O numero 3 apareceu na posiçao {n.index(3)+1}')
else:
     print(f'O nuemro 3 nao foi digitado')
print(f'Os numeros pares digitados foram:', end='')
for i in n:
     if i % 2 == 0:
          print(f'{i} ', end='')