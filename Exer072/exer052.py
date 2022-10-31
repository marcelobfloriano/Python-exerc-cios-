num = int(input("Digite um numero inteiro: "))
primo = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[34m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, primo))
if primo <= 2:
    print('{} é um numero primo'.format(num))
else:
    print("{} Nao é um numero primo".format(num))