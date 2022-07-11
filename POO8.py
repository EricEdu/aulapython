class Client:
    def __init__(self, nome: str, idade: int, sexo: str, salario: float):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario

        print(nome, idade, sexo, salario)

    def get_Sal(self):
        print("get salario", self.salario)

    def set_Sal(self, s):
        self.salario = s
        print("set salario", self.salario)

    mostrarclient = property(get_Sal, set_Sal)
meuclient = Client("Leo", 20, "Masculino", 1000)
meuclient.get_Sal()
meuclient.set_Sal(2000)
print(vars(meuclient))
        