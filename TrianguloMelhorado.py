class Triangulo:
    def __init__(self, LadoA: int, LadoB: int, LadoC: int, p: int):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
        self.p = p

    def setLado(self):
        self.LadoA = int(input("Valor do Primeiro lado: "))
        self.LadoB = int(input("Valor do Segundo lado: "))
        self.LadoC = int(input("Valor do Terceiro lado: "))

    def perimetro(self):
        self.p = (self.LadoA + self.LadoB + self.LadoC)

    def maiorlado(self):
        if (self.LadoA > self.LadoB) and (self.LadoA > self.LadoC):
            print("Maior ladoA")
        elif (self.LadoB > self.LadoA) and (self.LadoB > self.LadoC):
            print("Maior ladoB")
        elif (self.LadoC > self.LadoA) and (self.LadoC > self.LadoB):
            print("Maior LadoC")

    def tipo(self):
        if (self.LadoA == self.LadoB) and (self.LadoB == self.LadoC):
            print("Triangulo Equilatero")
        elif (self.LadoA != self.LadoB) and (self.LadoB != self.LadoC) and (self.LadoA != self.LadoA):
            print("Triangulo Escaleno")
        elif (self.LadoA == self.LadoB) and (self.LadoB != self.LadoC) or (self.LadoB == self.LadoC) and (self.LadoC != self.LadoA) or (self.LadoA == self.LadoC) and (self.LadoC != self.LadoB):
            print("Triangulo Isosceles")
        elif (self.LadoA > (self.LadoB + self.LadoC)) or (self.LadoB > (self.LadoA + self.LadoC)) or (self.LadoC > (self.LadoA + self.LadoB)):
            print("inexistente")

teste = Triangulo(0, 0, 0, 0)
teste.setLado()
teste.perimetro()
print(vars(teste))
teste.tipo()
teste.maiorlado()