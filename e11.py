rep = 4
for contador in range (rep): 
    p = float(input('peso: '))
    a = float(input('altura: '))
    imc = p/(a*a)
    if (imc< 18.5):
        print('abaixo do peso')
    elif (imc>=18.5 and imc<=24.9):
        print('peso normal')
    elif (imc>=25.0 and imc<=29.9):
        print('Excesso de peso')
    elif (imc>=30.0 and imc<=34.9):
        print('OBM')
    elif (imc>=35.0 and imc<=39.9):
        print('OBMII')
    elif (imc>=40.0):
        print('OBMIII')