class Id:
    """
    Classe permettant de générer des identifiants uniques
    """
    def __init__(self):
        self.num = 0
    #donne le prochain identifiant unique
    def nextId(self):
        self.num +=1
        return self.num - 1