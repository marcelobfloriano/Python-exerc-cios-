ptr = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(ptr, end=' → ')
        ptr = ptr + razao
        c += 1
    print('PAUSA')
    mais = int(input("Quantos termos quer a mais?: "))
print('PA finalizada com {} termos mostrados'.format(total))
