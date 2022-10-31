from datetime import date
atual = date.today().year
totM = 0
for c in range(0, 7):
    anoN = int(input("Em que ano a {}ª pessoa nasceu?: ".format(c + 1)))
    idade = atual - anoN
    if idade >= 21:
        totM += 1
print("{} pessoas SAO MAIORES DE IDADE".format(totM))
print("{} pessoas SAO MENORES DE IDADE".format(7 - totM))
