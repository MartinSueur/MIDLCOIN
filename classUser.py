# -*- coding: utf-8 -*-

from random import randint
from classPrivateKey import *
from classTransaction import *
from class32Point import *
from functions import hash32,find_trans_by_id,condition_hash_valide
from constantes import Gx,Gy

MAXRANDOMPRIVATEKEY = 100000
SOLDEINITIAL = 0


class User:
    def __init__(self,pseudo,identifiant):
        self.pseudo = pseudo
        self.id = identifiant
        e = randint(0,MAXRANDOMPRIVATEKEY)
        G = S32Point(Gx,Gy)
        self.clePrivee = PrivateKey(e)
        self.clePublique = e*G
        self.solde = SOLDEINITIAL
    
    def __str__(self):
        chaine = ""
        chaine += f"Utilisateur n°{self.id}\n"
        chaine += f"Pseudo : {self.pseudo}\n"
        chaine += f"Clé publique : {self.clePublique}\n"
        chaine += f"Solde : {self.solde}ϻ\n"
        return chaine
    
    def virement(self,user,montant,tip,identifiant):
        if montant >= 0 and tip >= 0:
            trans = Transaction(self,user,montant,tip,identifiant)
            message = int.from_bytes(hash32(f"{identifiant}{self.id}{user.id}{montant}{tip}".encode()),'big')
            sign = self.clePrivee.sign(message)
            return trans,sign
    
    