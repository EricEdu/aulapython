class Turma:
    def __init__(self, nome: str, codturma: int, horai: int, horaf: int):
        self.nome = nome
        self.codturma = codturma
        self.horai = horai
        self.horaf = horaf

    def montarturma(self):
        print(self.codturma, 'para montar uma turma')

    def sethora(self):
        self.horai = int(input('Hora de entrada da turma:'))
        self.horaf = int(input('Hora de saida da turma:'))

    def mostraturma(self):
        print(f'A turma: {self.nome}, com o codigo: {self.codturma}')

    def mostrahora(self):
        print(self.horai, 'horario de entrada', self.horaf, 'horario de saida')

test = Turma('TI', 3869, 0, 0)

test.montarturma()
test.mostraturma()
test.sethora()
test.mostrahora()




