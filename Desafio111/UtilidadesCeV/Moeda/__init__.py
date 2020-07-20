def aumentar (num=0, fator=0, format = False):
    result = num * (1+fator/100)
    return result if format is False else moeda(result)

def diminuir (num=0, fator=0, format = False):
    result = num * (1 - fator/100)
    return result if format is False else moeda(result)


def dobro(num=0, format = False):
    result = num*2
    return result if format is False else moeda(result)


def metade(num=0, format = False):
    result = num/2
    return result if format is False else moeda(result)


def moeda(preco, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(numero=0, au=10, di=20):
    print('-' * 30)
    print(f"{'Resumo do Valor':^30}")
    print('-' * 30)

    print(f"Preço analisado: \t{moeda(numero)}")
    print(f"Dobro do preço: \t{dobro(numero,True)}")
    print(f"Metade do preço: \t{metade(numero,True)}")
    print(f"{au} % de aumento: \t{aumentar(numero, au,True)}")
    print(f"{di} % de redução: \t{diminuir(numero, di,True)}")
    print('-' * 30)

