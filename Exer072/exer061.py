ptr = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
c = 1
print(ptr, end= ' → ')
while c < 10:
    ptr = ptr + razao
    c += 1
    print(ptr, end=' → ')
print('ACABOU')

'''decimo = ptr + (10 -1) * razao
for c in range(ptr, decimo + razao, razao):
    print(c, end=' → ')
print('ACABOU')'''