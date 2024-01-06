from classFieldElement import *
from constantes import *
"""
Element du corps fini Z/PZ, représenté en hexa sur 256bits
"""

class S256Field(FieldElement):
    def __init__(self,num, prime=None):
        super().__init__(num=num, prime=P)
    
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)