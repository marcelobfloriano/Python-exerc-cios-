from time import sleep
def maior(*num):
    maior = 0
    print('=-' * 20)
    print('ANALISANDO OS VALORES PASSADOS...')
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
        if num[c] > maior:
            maior = num[c]
        print(f'{num[c]}', end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'{maior} foi o maior valor informado')


maior(1,5,7,8,3)
maior()


