from leiaint import leiaint
from Desafio108 import moeda

print(f"\033[;1m{'Desafio 107 - Algumas funcoes matematicas':*^70}\033[m")
numero = 0

# loop para um menu facil
while True:
    escolha = leiaint('''
    1 - Criar/alterar numero
    2 - Seu Dobro
    3 - Sua Metade
    4 - Aumentar
    5 - Diminuir
    0 - Sair
    Escolha: ''',0,5)

    if escolha == 0:
        break
    if escolha == 1:
        numero = leiaint('Informe um numero: ')
    if escolha == 2:
        print(f"O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}")
    if escolha == 4:
        fator = leiaint('Informe o fator de aumento em %: ',0)
        print(f"Aumentar {fator}% de {moeda.moeda(numero)} resulta em {moeda.moeda(moeda.aumentar(numero,fator))}")
    if escolha == 5:
        fator = leiaint('Informe o fator de diminuição em %',0)
        print(f"Diminuir {fator}% de {moeda.moeda(numero)} resulta em {moeda.moeda(moeda.diminuir(numero,fator))}")
    if escolha == 3:
        print(f"A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}")


