from time import sleep

def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1 
    
    print('=-' * 18)
    print(f'Contagem de {a} a {b} de {c} em {c} ')
    
    
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.8)
            cont += c
    elif a > b:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.8)
            cont -= c
    print('FIM!')
    


    

contador(1,10,1)
contador(10,0,2)

print('=-' * 18)
print('AGORA É A SUA VEZ!!!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)