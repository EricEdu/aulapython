
rep = 5
for contador in range (rep):
    N = int(input('Numero: '))
    if (N<0):
        print('O Número Selecionado é Negativo')
    elif (N>0):
        print('O Número Selecionado é Positivo')
    elif (N == 0):
        print('O Número Selecionado é Neutro')
