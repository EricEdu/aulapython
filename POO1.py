class Fracao:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

a = Fracao(2, 3)
print(a)
b = Fracao(1, 4)
print(b)
        