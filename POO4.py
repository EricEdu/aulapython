class Aluno:
    def __init__(self, nome: str, curso: str, tempodes: int, temposd: int):
        self.nome = nome
        self.curso = curso
        self.tempodes = tempodes
        self.temposd = temposd

    def dormir(self, tempodes):
        self.tempodes += 4

    def estudar(self, temposd):
        self.temposd -= 2

    def mostraAluno(self):
        print(f'Nome: {self.nome}, Curso: {self.curso}, horas de estudo: {self.tempodes}, tempo sem dormir: {self.temposd}')

teste = Aluno('Carlos','ED.Parolar', 6, 8)

teste.mostraAluno()
teste.dormir(4)
teste.estudar(10)
teste.mostraAluno()


