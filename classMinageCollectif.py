from threading import *
from classMiner import *
from functions import *

class ThreadMiner(Thread):
    def __init__(self, mineur,heuristique=lambda x : x + 1):
        Thread.__init__(self)
        self.termine = False
        self.mineur = mineur
        self.resultat = -1
        self.heuristique=heuristique

    def run(self):
        bloc = self.mineur.liste_blocks[0]
        strHash = format32(bloc.get_hash())
        while not self.termine and not condition_hash_valide(strHash) :
            bloc.proof = self.heuristique(bloc.proof)
            strHash = format32(bloc.get_hash())
        
        if(condition_hash_valide(strHash)):
            self.resultat = bloc.proof
        else:
            self.resultat = -1

        