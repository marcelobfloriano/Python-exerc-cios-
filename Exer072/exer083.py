expr = (str(input('Digite uma expressao: ')))
pilha = []
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta correta!!')
else:
    print("Sua expressao esta incorreta!!!")