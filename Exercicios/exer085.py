num = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1} numero: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'O numeros pares sao: {num[0]}')
print(f'O numeros impares sao: {num[1]}')