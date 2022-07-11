maioralt = 0
menoralt = 1
maiorpeso = 0
menorpeso = 5
repeticoes = 5

for contador in range(repeticoes):

    peso = float(input('Peso:'))
    altura = float(input('Altura: '))
    if (altura > maioralt):
        maioralt = altura
    elif (altura < menoralt):
        menoralt = altura
    elif (peso>maiorpeso): 
         maiorpeso = peso
    elif (peso<menorpeso):
         menorpeso = peso

print('Maior altura:',maioralt)
print('Menor altura:',menoralt)
print('Maior peso:',maiorpeso)
print('Menor peso:',menorpeso)

    

