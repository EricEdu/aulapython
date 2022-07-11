class Professor:
    def __init__(self, nome: str, codprof: int, coddiscpl: int):
        self.nome = nome
        self.codprof = codprof
        self.coddiscpl = coddiscpl
        self.notas = 0

    def defprofessor(self):
        print('professor: ',self.nome,'com o codigo: ', self.codprof)

    def getnota(self):
        print('nota atual do aluno', self.notas)

    def setnota(self, n):
        self.notas = n
        print('nota atual redefinida do aluno:', self.notas)
    
    def mostraprof(self):
        print(f'O Professor {self.nome} está fazendo o log de professor com o codigo: {self.codprof} está acessando a disciplina com o codigo: {self.coddiscpl}.')

teste = Professor('Rogerio', 2347, 1225)

teste.defprofessor()
teste.mostraprof()

teste.getnota()
teste.setnota(10)