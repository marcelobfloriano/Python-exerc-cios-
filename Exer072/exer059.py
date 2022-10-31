val1 = int(input("Digite um valor: "))
val2 = int(input("Digite outro valor: "))
resultado = 0
maior = 0
while True:
    print("-=" * 15)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    print("-=" * 15)
    escolha = int(input("Qual sua opção?: "))
    print("-=" * 15)
    if escolha == 1:
        resultado = val1 + val2
        print('A soma entre {} + {} = {} '.format(val1, val2, resultado))
    elif escolha == 2:
        resultado = val1 * val2
        print('A multiplicaçao entre {} X {} = {} '.format(val1, val2, resultado))
    elif escolha == 3:
        if val1 > val2:
            maior = val1
            print('O maior valor = {} '.format(maior))
        elif val2 > val1:
            maior = val2
            print('O maior valor = {} '.format(maior))
    elif escolha == 4:
        val1 = int(input("Digite um valor: "))
        val2 = int(input("Digite outro valor: "))
    elif escolha == 5:
        print('ATE A PROXIMA')
        break
    else:
        print('OPCAO INVALIDA!!ESCOLHA  NOVAMENTE')

