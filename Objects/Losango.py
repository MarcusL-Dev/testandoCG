from Objects.Triangle import Triangle
from Objects.Object import Object

class Losango(Object):
    def __init__(self, cords, lengh, cor, invert, animates):
        super().__init__(cords, lengh, cor, invert, animates)

        self.trianguloSup = self.criaTriangulo(False)
        self.trianguloInf = self.criaTriangulo(True)

    def criaTriangulo(self, invert):
        return Triangle(
            [self.cords[0], self.cords[1]],
            self.lengh,
            self.cor,
            invert,
            [0, 1, 1]
        )

    def desenha(self):
        if len(self.animates) > 0: self.animate()
        self.trianguloSup.cor = self.cor
        self.trianguloInf.cor = self.cor
        self.trianguloSup.desenha()
        self.trianguloInf.desenha()





