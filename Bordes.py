from cmath import cos, pi, sin
import dis
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

class Nave(Modelo):

    posicion_borde_izq = [-1.18, -0.8, 0.0]
    posicion_borde_der = [1.18, -0.8, 0.0]

    def __init__(self):
        super().__init__(-1.18, -0.8, 0.0, 0.5, 0.0)
        self.extremo_izquierdo=0.05
        self.extremo_derecho=0.05
        self.extremo_inferior=0.05
        self.extremo_superior=0.05

    def dibujar(self):
        
        print('wtf')
        