
nomeNumeros = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
  while True:
    numero =  int(input("Digite um numero entre 0 a 20:"))
    if 0 <= numero <= 20:
      break
    print("Digite novamente!! ", end="")
  print(f'Voce digitou o numero {nomeNumeros[numero]}')

  resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
  if resp == 'N':
    break
print('-' * 40)
print('PROGRAMA ENCERRADO')