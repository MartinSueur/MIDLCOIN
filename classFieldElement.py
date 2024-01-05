class FieldElement:

    def __init__(self,num,prime):
        if num >= prime or num < 0:
            error = f"Nombre {num} n'est pas dans le corps qui va de 0 à {prime-1}"
            raise ValueError(error)
        self.num = num
        self.prime = prime
    
    def __repr__(self):
        return f'CF_{self.prime}({self.num})'
    
    def __eq__(self,other):
        if other is None:
            return False
        if other == 0:
            return (self.num==0)
        return self.num == other.num and self.prime == other.prime      
    
    def __ne__(self,other):
        return not (self == other)
    
    def __add__(self,other):
        if self.prime != other.prime:
            raise TypeError('On ne peut pas additionner deux nombres dans des corps différents')
        num = (self.num + other.num) % self.prime
        return self.__class__(num,self.prime)
    
    def __sub__(self,other):
        if self.prime != other.prime:
            raise TypeError('On ne peut pas soustraire deux nombres dans des corps différents')
        num = (self.num - other.num) % self.prime
        return self.__class__(num,self.prime)
    
    def __mul__(self,other):
        if self.prime != other.prime:
            raise TypeError('On ne peut pas multiplier deux nombres dans des corps différents')
        num = (self.num * other.num) % self.prime
        return self.__class__(num,self.prime)
    
    def __pow__(self,exponent):
        n = exponent % (self.prime -1)
        num = pow(self.num,n,self.prime)
        return self.__class__(num,self.prime)
    
    def __truediv__(self,other):
        if self.prime != other.prime:
            raise TypeError('On ne peut pas diviser deux nombres dans des corps différents')
        return self*(other)**(self.prime-2)
        