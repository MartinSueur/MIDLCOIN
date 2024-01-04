from classBlock import *
from functions import format32
from classBlockChain import *
import os

class Miner(User):
    def __init__(self,pseudo,identifiant):
        super().__init__(pseudo,identifiant)
        self.liste_blocks = []

    def voir_transactions(self,transactions):
        for trans in transactions:
            print(trans)
    
    def voir_blocks(self):
        chaine = ""
        for i in range(len(self.liste_blocks)):
            chaine+=f"Bloc n°{i}\n"
            chaine+=str(self.liste_blocks[i])
            chaine+="\n"
        print(chaine)
    
    def ajouter_transaction(self,block,transactions,id):
        trans = find_trans_by_id(transactions,id)
        if block.add_trans(trans):
            transactions.remove(trans)
            return True
        else:
            return False

    def construire_block(self,transactions,blockchain):
        id = 0
        if len(blockchain.blockchain) == 0:
            block = Block(0,self)
        else:
            block = Block(blockchain.lastBlock().get_hash(),self)
        while id != -1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Choisissez les transactions pour votre bloc puis -1 pour s'arreter.")
            print("Liste des transactions :")
            self.voir_transactions(transactions)
            id = int(input("Quelle transaction ajouter ? (id) : "))
            if id != -1 and self.ajouter_transaction(block,transactions,id):
                print("La transaction à été ajoutée.")
            else:
                if id != -1:
                    print("L'ajout de la transaction a échoué...")
            input("Appuyer sur Entrée pour continuer")
        self.liste_blocks.append(block)
        print("Le block a bien été enregistré.")
    
    def valider_block(self,proof,utilisateurs,blockchain): #pour le moment on peut valider que le premier bloc
        if len(self.liste_blocks) <= 0:
            return False
        block = self.liste_blocks[0]
        block.proof = proof
        hash = block.get_hash()
        strHash = format32(hash)
        if condition_hash_valide(strHash):
            blockchain.ajouter_block(block,utilisateurs,self)
            return True
        else:
            return False