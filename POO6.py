class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def aumentaSalario(self, salario):
        self.salario = self.salario + (self.salario * 0.5)

    def obtersal(self):
        return self.salario

    def mostraFuncionario(self):
        print(f'O funcionario: {self.nome}, recebe atualmente: {self.salario}')

teste = Funcionario('Roger',1000)

teste.mostraFuncionario()
teste.aumentaSalario(1)
teste.mostraFuncionario()

