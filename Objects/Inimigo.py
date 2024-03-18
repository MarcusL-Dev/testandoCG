import random
from Objects.Nave import Nave
from Objects.Projetil import Projetil

class Inimigo(Nave):
    def __init__(self, cords, lengh, cor, invert, rotate, animates, nivelInimigo):
        super().__init__(cords, lengh, cor, invert, rotate, animates)

        self.newPosition = 0
        self.nivelInimigo = nivelInimigo
    
    def atirar(self, scream):
        atirando = [True, False]
        if random.choice(atirando) and self.fireRate <= 0:
            projetil = Projetil([self.vertexs[1][0], self.vertexs[1][1]], 0.05, [1, 0, 1], [1, 0], 0, [], True)
            
            self.fireRate = 100-self.nivelInimigo
            if self.fireRate < 0:
                self.fireRate = 0
            scream.projeteis.append(projetil)
            
    def calcNewPosition(self):
        if (self.newPosition-0.1 < self.cords[0]) and (self.newPosition+0.1 > self.cords[0]):
            self.newPosition = round(random.uniform(-1+self.lengh/2, 1-self.lengh/2), 1)
        else:
            
            lado = self.cords[0] - self.newPosition
            if lado >= 0:
                self.cords[0] -= 0.01
            else:
                self.cords[0] += 0.01
        


