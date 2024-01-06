from threading import *
from classMiner import *
from functions import format256,condition_hash_valide
from heuristiques import *

class ThreadMiner(Thread):
    """
    Classe gérant un thread de minage par un mineur utilisant une heuristique
    """
    def __init__(self, mineur,heuristique=h_increment):
        Thread.__init__(self)
        self.termine = False
        self.mineur = mineur
        self.resultat = -1
        self.heuristique=heuristique
    #processus de minage
    def run(self):
        bloc = self.mineur.liste_blocks[0]
        strHash = format256(bloc.get_hash())
        while not self.termine and not condition_hash_valide(strHash) :
            bloc.proof = self.heuristique(bloc.proof)
            strHash = format256(bloc.get_hash())
        
        if(condition_hash_valide(strHash)):
            self.resultat = bloc.proof
        else:
            self.resultat = -1

        