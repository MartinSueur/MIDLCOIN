from classFieldElement import *
from constantes import *


class S32Field(FieldElement):
    def __init__(self,num, prime=None):
        super().__init__(num=num, prime=P)
    
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(8)