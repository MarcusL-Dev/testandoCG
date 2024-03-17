from Objects.Triangle import Triangle
from Objects.Projetil import Projetil

class Nave(Triangle):
    def __init__(self, cords, lengh, cor, invert, rotate, animates):
        super().__init__(cords, lengh, cor, invert, rotate, animates)
        self.fireHite = 0
        
    def atirar(self, scream):
        if self.fireHite <= 0:
            projetil = Projetil([(self.vertexs[1][0])-0.025, self.vertexs[1][1]], 0.05, [0, 1, 0], [0, 0], 0,  [], False, scream.ProjetilNumeroInit+1)
            scream.ProjetilNumeroInit = scream.ProjetilNumeroInit+1
            self.fireHite = 100
            scream.projeteis.append(projetil)

    def newPosition(self, lado):
        if lado == "esq" and self.cords[0] > -1:
            self.cords[0] = self.cords[0] - 0.01
        elif lado == "dir" and self.cords[0]+self.lengh < 1:
            self.cords[0] = self.cords[0] + 0.01


