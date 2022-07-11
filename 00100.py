class Cliente:
    def __init__(self,  nome, telefone, numero, saldo, limite):
        self.nome = str(nome)
        self.telefone = str(telefone)
        self.numero = str(numero)
        self.saldo = saldo
        self.limite = limite
        # inicia extrato
        self.extrato = []

    def mostraCliente(self):
        print(f'Nome: {self.nome}, telefone: {self.telefone}, Numero: {self.numero}, Saldo: {self.saldo}, limite: {self.limite}')
                
teste = Cliente('Ana','90999-0000',10029, 100.45, 3000.00)

teste.mostraCliente()
