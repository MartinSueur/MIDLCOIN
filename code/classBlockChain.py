from classBlock import *

class BlockChain:
    """
    Classe représentant la blockchain composée d'une liste de blocs
    """
    def __init__(self):
        self.blockchain = []
        self.halving = 100
    #représentation de la blockchain
    def __str__(self):
        chaine = ""
        fleche = "                       ||\n"
        for i in range(len(self.blockchain)):
            chaine+=f"Bloc n°{i} | miné par {self.blockchain[i].miner.pseudo}\n"
            chaine+=str(self.blockchain[i])
            if i != len(self.blockchain)-1:
                chaine+=fleche*3
                chaine+="                       \\/\n"
        return chaine
    #ajoute un bloc a la blockchain en effectuant ses opérations
    def ajouter_block(self,block,utilisateurs,miner):
        if (len(self.blockchain) == 0 and block.prev_hash == 0) or (not len(self.blockchain) == 0 and block.prev_hash == self.lastBlock().get_hash()):
            self.blockchain.append(block)
            for user in utilisateurs:
                user.liste_blocks = []
            for trans in block.transactions:
                trans.receveur.solde+=trans.montant
                trans.emetteur.solde-=trans.montant+trans.tip
                miner.solde+=trans.tip
            miner.solde+=self.halving
            self.update_halving()
        
    #met à jour le montant du halving à chaque ajout de bloc
    def update_halving(self):
        if len(self.blockchain)%4==0:
            self.halving/=2
    #retourne le dernier block de la blockchain
    def lastBlock(self):
        return self.blockchain[-1]

