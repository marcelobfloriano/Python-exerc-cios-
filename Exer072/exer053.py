frase = input('Digite uma frase: ').strip().upper() # strip tira os espaços  upper deixa maisuculo
palavras = frase.split() #O splip() separa a frase onde os espaços estão e cria uma lista só com as palavras, na ordem que aprecem.
junto = ''.join(palavras) # O join() junta string em uma lista, ou seja ele vai juntar as palavras que estão dentro da variável palavra
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('{} ao contrario é {}'.format(junto, inverso))
if junto == inverso:
    print("{} é um palíndromo".format(frase))
else:
    print("{} nao é um palíndromo".format(frase))
