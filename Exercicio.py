salario = float(input('Salário: '))
newsal = 0
if(salario<500):
    newsal = salario+salario * (15/100)
elif(salario >= 500 and salario <= 1000):
    newsal = salario + salario * (10/100)
elif(salario > 1000):
    newsal = salario + salario * (5/100) 
print('Novo salario: ',newsal)








