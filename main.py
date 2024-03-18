from OpenGL.GL import *
from OpenGL.GLUT import *
from Objects.Nave import Nave
from Objects.Inimigo import Inimigo
import random
import math

class Program:
    def __init__(self):
        self.teclas = [False, False]
        
        self.nave = Nave(
            [0, -0.75], 0.25, [0, 0, 1], [0, 0], 0,  []
        )
        self.inimigos = []
        self.projeteis = []
        
        self.nivelInimigo = 1
        
        self.numInimigosMortos = 0

    def criaInimigo(self):
        return Inimigo(
            [0, 0.75], 0.25, [1, 0, 0], [1, 0], 0,  [], self.nivelInimigo
        )
        
    def geraInimigos(self, num):
        for i in range(num):
            self.inimigos.append(self.criaInimigo())

    def keyboardUp(self, key, x, y):
        if key == key == b'a':
            self.teclas[0] = not self.teclas[0]
        elif key == b'd':
            self.teclas[1] = not self.teclas[1]

    def keyboard(self, key, x, y):
        if key == b'k':
            self.nave.atirar(self)
        elif key == key == b'a':
            self.teclas[0] = not self.teclas[0]
        elif key == b'd':
            self.teclas[1] = not self.teclas[1]
        
    def desenhaNave(self):
        self.nave.fireHite = self.nave.fireHite - 1
        if self.teclas[0]:
            self.nave.newPosition("esq")
        if self.teclas[1]:
            self.nave.newPosition("dir") 
        self.nave.desenha()
        
    def desenhaInimigos(self):
        lados = ["esq", "dir"]
        for inimigo in self.inimigos:
            inimigo.fireHite = inimigo.fireHite - 1
            lado = random.choice(lados)
            inimigo.newPosition(lado)
            inimigo.atirar(self)
            inimigo.desenha()
            
    def desenhaProjeteis(self):
        for projetil in self.projeteis:
            projetil.newPosition()
            projetil.desenha()
            
    def deletaProjeteis(self):
        for projetil in self.projeteis:
            if projetil.cords[1] > 1 or projetil.cords[1] < -1:
                self.projeteis.remove(projetil)
                
    def detectaColisoes(self):
        for inimigo in self.inimigos:
            for projetil in self.projeteis:
                if projetil.isEnemy != True:
                    distancia = math.sqrt((inimigo.cords[0] - projetil.cords[0])**2 + (inimigo.cords[1] - projetil.cords[1])**2)
                    if distancia <= (inimigo.lengh/2)+(projetil.lengh/2):
                        self.inimigos.remove(inimigo)
                        self.projeteis.remove(projetil)
                        self.geraInimigos(1)
                        self.nivelInimigo += 1
                        self.numInimigosMortos += 1
                        print(self.numInimigosMortos)
                        
        for projetil in self.projeteis:
            if projetil.isEnemy:
                distancia = math.sqrt((self.nave.cords[0] - projetil.cords[0])**2 + (self.nave.cords[1] - projetil.cords[1])**2)
                if distancia <= (self.nave.lengh/2)+(projetil.lengh/2):
                    glutLeaveMainLoop()
        
    def desenha(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        
        self.desenhaNave()
        self.desenhaInimigos()
        self.desenhaProjeteis()
        
        self.detectaColisoes()
        self.deletaProjeteis()

        glutSwapBuffers()
        
    def inicio(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow('testando')
        glClearColor(0,0,0,1)
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
        self.geraInimigos(3)
        glutDisplayFunc(self.desenha)
        glutIdleFunc(self.desenha)
        glutKeyboardFunc(self.keyboard)
        glutKeyboardUpFunc(self.keyboardUp)
        glutMainLoop()

    def run(self):
        self.inicio()        

Program().run()
