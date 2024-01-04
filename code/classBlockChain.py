from classBlock import *

class BlockChain:
    def __init__(self):
        self.blockchain = []
        self.halving = 100
    
    def __str__(self):
        chaine = ""
        fleche = "                       ||\n"
        for i in range(len(self.blockchain)):
            chaine+=f"Bloc n°{i} | miné par {self.blockchain[i].miner.pseudo}\n"
            chaine+=str(self.blockchain[i])
            if i != len(self.blockchain)-1:
                chaine+=fleche*3
                chaine+="                       v\n"
        return chaine

    def ajouter_block(self,block,utilisateurs,miner): #TODO : effectuer les transactions du block ajouté
        self.blockchain.append(block)
        for user in utilisateurs:
            user.liste_blocks = []
        for trans in block.transactions:
            trans.receveur.solde+=trans.montant
            trans.emetteur.solde-=trans.montant+trans.tip
            miner.solde+=trans.tip
        miner.solde+=self.halving
        self.update_halving()
        
        
    def update_halving(self):
        if len(self.blockchain)%4==0:
            self.halving/=2

    def lastBlock(self):
        return self.blockchain[-1]

