def leiadinheiro(msg):
    valido = False
    while not valido:
        #pede ao usuario uma string sem os espaços
        entrada = str(input(msg)).replace(',','.').strip()
        # Se for alfa retorna error.
        if entrada.isalpha() or entrada == '':
            print("Error!")
        # Se não for, retorna um float
        else:
            valido = True
            return float(entrada)