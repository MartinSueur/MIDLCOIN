class Signature:
    """
    Représente une signature d'un message par un utilisateur
    """
    def __init__(self, r, s):
        self.r = r
        self.s = s
    #réprésente en hexa une signature
    def __repr__(self):
        return 'Signature({:x},{:x})'.format(self.r, self.s)