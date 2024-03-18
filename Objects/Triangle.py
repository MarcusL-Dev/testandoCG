from OpenGL.GL import *
from Objects.Object import Object

class Triangle(Object):
    def calcVertexs(self):
        return [
            [self.cords[0]-self.lengh/2, self.cords[1]-self.lengh/2],
            [self.cords[0], self.cords[1]+self.lengh/2],
            [self.cords[0]+self.lengh/2, self.cords[1]-self.lengh/2]
        ]    

    def inverterVertical(self):
        aux = self.vertexs[1][1]
        self.vertexs[1][1] = self.vertexs[0][1]
        self.vertexs[0][1] = aux
        self.vertexs[2][1] = aux

    def inverterHorizontal(self):
        pass

    def inverter(self):
        if self.invert[0]:
            self.inverterVertical()

        if self.invert[1]:
            self.inverterHorizontal()

    def rotater(self):
        pass

    def desenha(self):
        self.vertexs = self.calcVertexs()
        if len(self.invert) > 0: self.inverter()
        if self.rotate > 0: self.rotater()
        if len(self.animates) > 0: self.animate()

        glColor3f(self.cor[0], self.cor[1], self.cor[2])
        glBegin(GL_TRIANGLES)

        for vertex in self.vertexs:
            glVertex2f(vertex[0], vertex[1])

        glEnd()


