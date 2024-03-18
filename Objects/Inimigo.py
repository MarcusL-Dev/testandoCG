import random
from Objects.Nave import Nave
from Objects.Projetil import Projetil

class Inimigo(Nave):
    def atirar(self, scream):
        atirando = [True, False]
        if random.choice(atirando) and self.fireHite <= 0:
            projetil = Projetil([self.vertexs[1][0]-0.025, self.vertexs[1][1]], 0.05, [1, 0, 1], [1, 0], 0,  [], True)
            self.fireHite = 100
            scream.projeteis.append(projetil)


