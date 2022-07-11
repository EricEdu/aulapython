nomes = ['Ana','Pedro','José','Maria']
notas = [9.0,8.0,7.0,6.0]

soma = 0
for nota in notas:
    soma += nota
media = soma/len(notas)
print('Media da turma: ', media)
for i in range(len(notas)):
    if notas[i]> media:
        print('Aluno com nota acima da média: ', nomes[i],'Nota:', notas[i] )