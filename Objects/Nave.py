from Objects.Triangle import Triangle
from Objects.Projetil import Projetil

class Nave(Triangle):
    def __init__(self, cords, lengh, cor, invert, rotate, animates):
        super().__init__(cords, lengh, cor, invert, rotate, animates)
        self.fireRate = 0
        self.fireRateCheio = 100
        
    def atirar(self, scream):
        if self.fireRate <= 0:
            projetil = Projetil([self.vertexs[1][0], self.vertexs[1][1]], 0.05, [0, 1, 0], [0, 0], 0,  [], False)
            self.fireRate = self.fireRateCheio
            scream.projeteis.append(projetil)

    def calcNewPosition(self, lado):
        if lado == "esq" and self.cords[0]-self.lengh/2 > -1:
            self.cords[0] = self.cords[0] - 0.01
        elif lado == "dir" and self.cords[0]+self.lengh/2 < 1:
            self.cords[0] = self.cords[0] + 0.01
            
    def upgrade(self, tipo, scream):
        if scream.numUpgrades > 0:
            if tipo == 1:
                self.fireRateCheio -= 2
                if self.fireRateCheio < 0:
                    self.fireRateCheio = 0
            else:
                scream.numEscudos += 1
            scream.numUpgrades -= 1


