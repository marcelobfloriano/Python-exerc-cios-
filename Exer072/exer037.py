numero = int(input("Digite um numero: "))
escolha = int(input('''Digite: 
1. para binário 
2. para octal  
3. para hexadecimal
Digite sua opçao:'''))
if escolha == 1:
    print('{} convertido para BINARIO fica: {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para octadecimal fica: {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal fica: {}'.format(numero, hex(numero)[2:]))
else:
    print('Opcao invalida!!!')
