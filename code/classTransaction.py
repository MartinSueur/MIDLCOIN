# -*- coding: utf-8 -*-

from functions import *

class Transaction:
    """
    Clase représentant une transaction d'un montant depuis un emetteur vers un receveur avec pourboire
    chaque transaction possède un identifiant unique
    """
    def __init__(self,emetteur,receveur,montant,tip,identifiant):
        self.emetteur = emetteur
        self.receveur = receveur
        self.montant = montant
        self.tip = tip
        self.id = identifiant
    #représente une transaction
    def __repr__(self): #peut pas mettre de parenthèses... chokbar de l'erreur
        return f"Transaction n°{self.id} : {self.emetteur.pseudo} paye {self.receveur.pseudo} {self.montant}ϻ. (Tip:{self.tip}ϻ)"
    #renvoie le hash d'une transaction contenant toutes ses informations
    def getMessage(self):
        return int.from_bytes(hash256(f"{self.id}{self.emetteur.id}{self.receveur.id}{self.montant}{self.tip}".encode()),'big')