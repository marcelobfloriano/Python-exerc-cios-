from datetime import date 
def voto(a):
    global idade
    ano = date.today().year
    idade = ano - a
    if idade < 16:
        return "Negado"
    elif idade >= 16 and idade < 18:
        return "Opcional"
    elif idade >= 18:
        return "Obrigatorio"

ano = int(input('Digite o ano do seu nascimento: '))
resultado = voto(ano)
print(f' Com {idade} anos seu voto é {resultado}')
