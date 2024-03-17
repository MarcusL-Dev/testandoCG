import random
import time

class Object:
    def __init__(self, cords, lengh, cor, invert, rotate, animates):
        self.cords = cords
        self.lengh = lengh
        self.cor = cor

        self.rotate = rotate
        self.invert = invert

        self.animates = animates

        self.vertexs = []

    def colorAnimate(self):
        corAMudar = random.randint(1, 3)
        if corAMudar == 1: self.cor = [1, 0, 0]
        if corAMudar == 2: self.cor = [0, 1, 0]
        if corAMudar == 3: self.cor = [0, 0, 1]

    def lenghAnimate(self):
        self.lengh = self.lengh + 0.01

    def animate(self):
        time.sleep(0.1)
        if self.animates[0]: self.colorAnimate()
        if self.animates[1]: self.lenghAnimate()
        if self.animates[2]: self.cordsAnimate()

    def calcVertexs(self):
        pass

    def desenha(self):
        pass
