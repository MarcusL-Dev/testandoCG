from Objects.Triangle import Triangle

class Projetil(Triangle):
    def __init__(self, cords, lengh, cor, invert, rotate, animates, isEnemy, numero):
        super().__init__(cords, lengh, cor, invert, rotate, animates)
        self.isEnemy = isEnemy
        self.numero = numero
    
    def newPosition(self):
        if self.isEnemy:
            self.cords[1] = self.cords[1] - 0.01
        else:
            self.cords[1] = self.cords[1] + 0.01

