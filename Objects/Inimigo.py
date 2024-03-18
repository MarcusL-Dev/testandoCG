import random
from Objects.Nave import Nave
from Objects.Projetil import Projetil

class Inimigo(Nave):
    def __init__(self, cords, lengh, cor, invert, rotate, animates, nivelInimigo):
        super().__init__(cords, lengh, cor, invert, rotate, animates)
    
        self.nivelInimigo = nivelInimigo   
    
    def atirar(self, scream):
        atirando = [True, False]
        if random.choice(atirando) and self.fireHite <= 0:
            projetil = Projetil([self.vertexs[1][0]-0.025, self.vertexs[1][1]], 0.05, [1, 0, 1], [1, 0], 0,  [], True)
            
            self.fireHite = 100-self.nivelInimigo
            if self.fireHite < 0:
                self.fireHite = 0
            scream.projeteis.append(projetil)


