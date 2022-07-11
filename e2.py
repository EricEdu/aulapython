print('Calcular media de 3 notas.\n')
n1 = float(input('N1:'))
n2 = float(input('N2:'))
n3 = float(input('N3:'))
media = (n1 + n2 + n3)/3
print('media:', media)
if (media<5.0):
    print('Reprovado')
elif (media>=7.0):
    print('Aprovado')
else:
    print('Recuperação')