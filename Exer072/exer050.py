sp = 0 # soma dos par
qpd = 0 # quantidade de par
for c in range(0, 6): # c contador
    num = int(input("Digite o {}ª Valor: ".format(c +1))) # alt + 166 = ª
    if num % 2 == 0:
        sp += num
        qpd += + 1
if qpd > 0:
    print('''Quantidade de par digitado: {} 
Total da soma: {} '''.format(qpd, sp))
else:
    print("Nenhum numero par digitado")