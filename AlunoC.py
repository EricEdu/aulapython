class Aluno:
    def __init__(self, nome: str, matri: int, cdturm: int):
        self.nome = nome
        self.matri = matri
        self.cdturm = cdturm

    def cadastro(self):
        print("O aluno", self.nome,"esta cadastrado ") 

    def matricula(self):
        print("O numero de matricula do aluno é", self.matri)

    def aula(self):
        print("Acesso a o calendario de aulas com o codigo: ", self.cdturm)

    def mostraaluno(self):
        print(f'O aluno {self.nome} com o numero de matricula: {self.matri} está acessando o calendario de aulas com o codigo de turma: {self.cdturm}.')

teste = Aluno('rodivaldo', 12345, 9876)

teste.cadastro()
teste.matricula()
teste.aula()
teste.mostraaluno()

    