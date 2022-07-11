class Curso:
    def __init__(self, nome: str, codcurso: int, codturma: int, coddiscpl: int):
        self.nome = nome
        self.codcurso = codcurso
        self.codturma = codturma
        self.coddiscpl = coddiscpl


    def montarcurso(self):
        print('Codigo do curso: ',self.codcurso,' com as disciplinas: ', self.coddiscpl)

    def organizar(self):
        print('curso oganizado utilizando o codigo de turma', self.codturma)

    def mostracurso(self):
        print(f'O Curso:{self.nome} Codigo do curso:{self.codcurso}, com as disciplinas: {self.coddiscpl} na turma: {self.codturma}.')

test = Curso('TI', 67346, 2378, 1645)

test.mostracurso()
test.montarcurso()
test.organizar()