class Triangulo:
    def __init__(self, LadoA: int, LadoB: int, LadoC: int, p: int):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
        self.p = p

        print(LadoA, LadoB, LadoC)

    def perimetro(self):
        self.p = (self.LadoA + self.LadoB + self.LadoC)

    def maiorlado(self):
        if (self.LadoA > self.LadoB) and (self.LadoA > self.LadoC):
            print("Maior ladoA")
        elif (self.LadoB > self.LadoA) and (self.LadoB > self.LadoC):
            print("Maior ladoB")
        elif (self.LadoC > self.LadoA) and (self.LadoC > self.LadoB):
            print("Maior LadoC")

teste = Triangulo(10, 10, 15, 0)
teste.perimetro()
teste.maiorlado()
print(vars(teste))

        