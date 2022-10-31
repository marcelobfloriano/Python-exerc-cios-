ccin = cvin = cdez = cdum = aux = 0
saque = int(input("Qual valor do saque: R$ "))
while 0 < saque >= 50:
    saque -= 50
    aux = saque
    saque = aux
    ccin += 1
    if saque == 0:
        break
while 0 < saque >= 20:
    saque -= 20
    aux = saque
    saque = aux
    cvin += 1
    if saque == 0:
        break
while 0 < saque >= 10:
    saque -= 10
    aux = saque
    saque = aux
    cdez += 1
    if saque == 0:
        break
while 0 < saque >= 1:
    saque -= 1
    aux = saque
    saque = aux
    cdum += 1
    if saque == 0:
        break
print(f'{ccin} notas de R$ 50')
print(f'{cvin} notas de R$ 20')
print(f'{cdez} notas de R$ 10')
print(f'{cdum} notas de R$ 01')

