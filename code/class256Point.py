from classPoint import *
from class256Field import *
from class256Point import *
from constantes import *

"""
Cette classe permet de représenter des points sur la courbe elliptique défini sur un corps fini
"""


class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)
    #multiplication scalaire à droite
    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)
    #multiplication scalaire à gauche
    def __mul__(self, coefficient):
        coef = coefficient % N
        return super().__mul__(coef)
   #représentation 
    def __repr__(self):
        if self.x == None:
            return f"infini"
        else:
            return f"({self.x},{self.y})"
    #permet de verifier la validité d'une signature à partir de la clé publique et du message
    def verify(self, z, sig):
        G = S256Point(Gx,Gy)
        s_inv = pow(sig.s, N - 2, N) #petit théorème de fermat et identité de Bezout
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u * G + v * self
        return total.x.num == sig.r