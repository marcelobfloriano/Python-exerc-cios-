while True:
    print('''FACA SUA ESCOLHA
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')
    eUsu = int(input())
    from random import randint
    itens = ("Pedra", "Papel","Tesoura")
    eCpu = randint(0, 2)

    eUsu = eUsu - 1

    if eUsu == eCpu:
        print("{} X {} EMPATE!!!".format(itens[eUsu], itens[eCpu]))
    elif eUsu == 0 and eCpu == 1:
        print("{} X {} CPU VENCEU!!!".format(itens[eUsu], itens[eCpu]))
    elif eUsu == 0 and eCpu == 2:
        print("{} X {} VOCE VENCEU!!!".format(itens[eUsu], itens[eCpu]))
    elif eCpu == 0 and eUsu == 1:
        print("{} X {} VOCE VENCEU!!!".format(itens[eUsu], itens[eCpu]))
    elif eCpu == 0 and eUsu == 2:
        print("{} X {} CPU VENCEU!!!".format(itens[eUsu], itens[eCpu]))
    else:
        print("Jogada Invalida!!!")

