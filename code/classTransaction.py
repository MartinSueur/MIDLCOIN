# -*- coding: utf-8 -*-

from functions import *

class Transaction:
    def __init__(self,emetteur,receveur,montant,tip,identifiant):
        self.emetteur = emetteur
        self.receveur = receveur
        self.montant = montant
        self.tip = tip
        self.id = identifiant

    def __repr__(self): #peut pas mettre de parenthèses... chokbar de l'erreur
        return f"Transaction n°{self.id} : {self.emetteur.pseudo} paye {self.receveur.pseudo} {self.montant}ϻ. (Tip:{self.tip}ϻ)"
    
    def getMessage(self):
        return int.from_bytes(hash32(f"{self.id}{self.emetteur.id}{self.receveur.id}{self.montant}{self.tip}".encode()),'big')