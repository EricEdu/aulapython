lista = [2,7,8,9,7]
valorprocurado = 8
for i in range(len(lista)):
    if valorprocurado == lista[i]:
        print("valor procurado indice: ", i)
    else:
        print("Diferente")