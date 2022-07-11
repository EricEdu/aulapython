class Livro:
    def __init__(self, nome: str, qtdpg: int, autor: str, preco: float):
        self.nome = nome
        self.qtdpg = qtdpg
        self.autor = autor
        self.preco = preco
        print(nome, qtdpg, autor, preco)

    def getPreco(self):
        print("get preco", self.preco)

    def setPreco(self, p):
        self.preco = p
        print("set preco", self.preco)

    mostrarpreco = property(getPreco, setPreco)
meulivro = Livro("Livro M", 320, "MT peixoto", 25)
meulivro.getPreco()
meulivro.setPreco(15)
print(vars(meulivro))
        