from classPoint import *
from class32Field import *
from class32Point import *
from constantes import *




class S32Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S32Field(A), S32Field(B)
        if type(x) == int:
            super().__init__(x=S32Field(x), y=S32Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)
    
    def __mul__(self, coefficient):
        coef = coefficient % N
        return super().__mul__(coef)
    
    def __repr__(self):
        if self.x == None:
            return f"infini"
        else:
            return f"({self.x},{self.y})"
    
    def verify(self, z, sig):
        G = S32Point(Gx,Gy)
        s_inv = pow(sig.s, N - 2, N)
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u * G + v * self
        return total.x.num == sig.r