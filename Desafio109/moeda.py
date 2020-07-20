def aumentar (num=0, fator=0, format = False):
    result = num * (1+fator/100)
    # joga o resultado na função moeda, a qual o transforma em uma string bem formatada
    return result if format is False else moeda(result)


def diminuir (num=0, fator=0, format = False):
    result = num * (1 - fator/100)
    # joga o resultado na função moeda, a qual o transforma em uma string bem formatada
    return result if format is False else moeda(result)


def dobro(num=0, format = False):
    result = num*2
    # joga o resultado na função moeda, a qual o transforma em uma string bem formatada
    return result if format is False else moeda(result)


def metade(num=0, format = False):
    result = num/2
    # joga o resultado na função moeda, a qual o transforma em uma string bem formatada
    return result if format is False else moeda(result)


# Programa que retorna um valor em string muito bem formatado
def moeda(preco, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


