class Funcionario:
    
    def __init__(self, nome: str, cpf: str, salario: float, desconto: float, salarioliquido: float):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.desconto = desconto
        self.salarioliquido = salarioliquido

    def descontar(salario, desconto,salarioliquido):
        desconto = salario*(desconto)
        salarioliquido = salario-desconto
        return salarioliquido

    def mostraFuncionario(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, salario: {self.salario} reais, Desconto: {self.desconto}, salárioliquido: {self.salarioliquido}')
    
marcos = Funcionario('Marcos', '12222', 2500, 0.05, 2375)
marcos.mostraFuncionario()


    
       
        

