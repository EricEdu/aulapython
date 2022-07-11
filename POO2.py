class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade 
        self.altura = altura

    def mostraPessoa(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura}.')
pessoa = Pessoa(nome='João', idade =25, altura=1.88)
pessoa.mostraPessoa()
       