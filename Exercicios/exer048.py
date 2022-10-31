cs = 0
cont = 0
for c in range(1, 500, 2): # usou o 2 pq vou querer numeros impares para esse programa exe 1 + 2 = 3, 5, 7, 9
    if c % 3 == 0:
        cs += c
        cont += 1
print('Total de {} multiplicadores de 3 entre 1 ao 500 somados sao: {}'.format(cont, cs))