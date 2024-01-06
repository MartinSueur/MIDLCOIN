class Point:
    """
    Un point sur une courbe elliptique d'équation y^2 = x^3 + ax + b
    """

    def __init__(self,x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return 
        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError(f"({self.x},{self.y}) n'est pas sur la courbe")
    
    #représentation d'un point
    def __repr__(self):
        if self.x == None:
            return f"(infini sur a={self.a},b={self.b})"
        else:
            return f"({self.x},{self.y}) sur a={self.a},b={self.b}"
    #égalité
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    #inégalité
    def __ne__(self, other):
        return not(self == other)
    #addition
    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f"Les points {self}, {other} ne sont pas sur la même courbe")
        elif self.x is None:
            return other
        elif other.x is None:
            return self
        elif self.x != other.x:
            s = (other.y - self.y)/(other.x-self.x)
            x = (s**2 - self.x - other.x)
            y = s*(self.x - x) - self.y
            return self.__class__(x,y,self.a,self.b)
        elif self == other:
            if self.y == 0:
                return self.__class__(None,None,self.a,self.b)
            s = ((self.x**2)+(self.x**2)+(self.x**2)+self.a)/(self.y+self.y)
            x = (s**2 - self.x - self.x)
            y = s*(self.x - x) - self.y
            return self.__class__(x,y,self.a,self.b)
        else:
            return self.__class__(None,None,self.a,self.b)
    #multiplication scalaire à gauche
    def __mul__(self,coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
    #multiplication scalaire à droite
    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
