# -*- coding: utf-8 -*-

from random import randint
from classPrivateKey import *
from classTransaction import *
from class256Point import *
from functions import hash256

MAXRANDOMPRIVATEKEY = 100000
SOLDEINITIAL = 0


class User:
    """
    Classe représentant un utilisateur avec un pseudo et un identifiant, on génère sa clé privée aléatoirement
    """
    def __init__(self,pseudo,identifiant):
        self.pseudo = pseudo
        self.id = identifiant
        e = randint(0,MAXRANDOMPRIVATEKEY)
        self.clePrivee = PrivateKey(e)
        self.clePublique = self.clePrivee.point
        self.solde = SOLDEINITIAL
    #permet d'afficher le profil d'un utilisateur
    def __str__(self):
        chaine = ""
        chaine += f"Utilisateur n°{self.id}\n"
        chaine += f"Pseudo : {self.pseudo}\n"
        chaine += f"Clé publique : {self.clePublique}\n"
        chaine += f"Solde : {self.solde}ϻ\n"
        return chaine
    #permet de réaliser et signer une transaction
    def virement(self,user,montant,tip,identifiant):
        if montant >= 0 and tip >= 0:
            trans = Transaction(self,user,montant,tip,identifiant)
            message = int.from_bytes(hash256(f"{identifiant}{self.id}{user.id}{montant}{tip}".encode()),'big')
            sign = self.clePrivee.sign(message)
            return trans,sign
    
    