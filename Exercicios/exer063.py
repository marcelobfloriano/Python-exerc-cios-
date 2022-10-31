termos = int(input('Quantos termos quer mostrar?: '))
ptr = 0
sgtr = 1
ter = 0
print(ptr, end=' → ')
print(sgtr, end=' → ')
c = 2
while c < termos:
    ter = ptr + sgtr
    print(ter, end=' → ')
    ptr = sgtr
    sgtr = ter
    c += 1
print('ACABOU')