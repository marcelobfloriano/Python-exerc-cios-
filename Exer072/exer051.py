ptr = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
decimo = ptr + (10 -1) * razao
for c in range(ptr, decimo + razao, razao):
    print(c, end=' → ')
print('ACABOU')