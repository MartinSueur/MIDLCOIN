from classUser import *
from classTransaction import *

MAXTRANSPARBLOCK=20

class Block:
    """
    Classe représentant les blocs de la blockchain
    Un bloc est composé : du hash du bloc précédent,d'un ensemble de transactions, une preuve de travail et un mineur 
    """
    def __init__(self,prev_hash,miner):
        self.transactions = []
        self.prev_hash = prev_hash
        self.proof = -1
        self.block_users = []
        self.miner = miner
    #affichage d'un bloc
    def __str__(self):
        chaine = ""
        ligne = "--------------------------------------------------\n"
        chaine+=ligne
        chaine+=str(self.prev_hash)+"\n"
        chaine+=ligne
        if len(self.transactions)==0:
            chaine+="Aucune transaction\n"
        for trans in self.transactions:
            chaine+=str(trans)+"\n"
        chaine+=ligne
        if self.proof==-1:
            chaine+="A déterminer...\n"
        else:
            chaine+=str(self.proof)+"\n"
        chaine+=ligne
        return chaine
    #ajout d'un utilisateur (fantôme) au bloc 
    def add_user_to_bloc(self,user):
        dedans = False
        for other in self.block_users:
            if user.id == other.id:
                dedans = True
        if not dedans:
            copie = User(user.pseudo,user.id)
            copie.solde = user.solde
            self.block_users.append(copie)
    #renvoie un utilisateur par son identifiant
    def find_user_by_id(self,id):
        for user in self.block_users:
            if user.id == id:
                return user
        return -1
    #ajoute une transaction a un bloc si elle est faisable : on vérifie si l'emetteur possède assez de MIDLCOIN pour la transaction
    def add_trans(self,transaction):
        if len(self.transactions)>=MAXTRANSPARBLOCK:
            return False
        emetteur = transaction.emetteur
        receveur = transaction.receveur
        self.add_user_to_bloc(emetteur)
        self.add_user_to_bloc(receveur)
        copieE = self.find_user_by_id(emetteur.id)
        copieR = self.find_user_by_id(receveur.id)
        copieE.solde -= transaction.montant+transaction.tip
        if copieE.solde < 0:
            copieE.solde += transaction.montant+transaction.tip
            return False
        else:
            copieR.solde += transaction.montant+transaction.tip
            self.transactions.append(transaction)
            return True
    #retourne le hash du bloc en concatenant tout ce qui le compose (sauf le mineur)
    def get_hash(self):
        chaine = ""
        chaine+=str(self.prev_hash)
        for trans in self.transactions:
            chaine+=str(trans.getMessage())
        chaine+=str(self.proof)
        return int.from_bytes(hash256(chaine.encode()),'big')
    #retourne la somme de tous les pourboires d'un bloc
    def get_total_tip(self):
        total = 0
        for trans in self.transactions:
            total+=trans.tip
        return total