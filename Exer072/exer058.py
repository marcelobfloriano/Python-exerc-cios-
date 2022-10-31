from random import randint
numeroCpu = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar num numero de 0 a 10')
print('Sera que voce consegue advinhar qual foi?')
numeroUsu = int(input('Qual seu palpite?: '))
numPalpite = 1
while numeroUsu != numeroCpu:
    if numeroUsu > numeroCpu:
        print('Menos... um numero menor')
    elif numeroUsu < numeroCpu:
        print('Mais... um numero maior')
    numeroUsu = int(input('Tente novamente: '))
    print('Qual seu palpite?: ')
    numPalpite += 1

print('Voce acertou!!! Depois de {} palpites'.format(numPalpite))

