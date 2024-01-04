# -*- coding: utf-8 -*-

from classId import *
from class32Field import *
from class32Point import *
from constantes import *
from classPrivateKey import *
from classSignature import *
from classUser import *
from classMiner import *
from functions import miner
from threading import *
from classMinageCollectif import *

def diffuserVirement(virement):
   trans = virement[0]
   sign = virement[1]
   #if trans.emetteur.clePublique.verify(trans.getMessage(),sign):
   transactions.append(trans)

def voir_user(user):
   print(f"Utilisateur n°{user.id} : {user.pseudo}")

def voir_registre_users(users):
   for user in users:
      voir_user(user)

def get_total_tip(block):
   total= 0
   for trans in block.transactions:
      total+=trans.tip
   return total

def thread_verification(liste_threads):
   termine = False
   while not termine :
      for threads in liste_threads :
         print(threads.mineur.liste_blocks[0].proof, threads)
         if threads.resultat > 0 :
            termine = True

   for threads in liste_threads :
      threads.termine = True


def lancer_minage_collectif(utilisateurs):
   liste_mineurs_actifs = []
   liste_threads = []
   for mineur in utilisateurs :
      if len(mineur.liste_blocks) > 0 :
         liste_mineurs_actifs.append(mineur)
         liste_threads.append(ThreadMiner(mineur))

   verif = Thread(target=thread_verification, args=[liste_threads])

   verif.start()

   for threads in liste_threads :
      threads.start()

   verif.join()   
      
   for threads in liste_threads :
      threads.join()

   for threads in liste_threads :
      if threads.resultat != -1 :
         print(f"Le mineur le plus rapide est : {threads.mineur.pseudo}")
         threads.mineur.valider_block(threads.resultat, utilisateurs, BLOCKCHAIN) 
         print("Le bloc a été validé")
         input("Appuyez pour continuer...")

def session_utilisateur(active_user):
   j=0
   while j!=6:
      os.system('cls' if os.name == 'nt' else 'clear')
      j = intInput("Que souhaitez vous faire ?\n 1 - Consulter son profil\n 2 - Faire un virement\n 3 - Constuire un bloc\n 4 - Miner un bloc\n 5 - Consulter la Blockchain\n 6 - Quitter\n")
      if j==1:
         print(active_user)
         input("Appuyez sur Entrée pour continuer")
      elif j==2:
         voir_registre_users(utilisateurs)
         ident = intInput("Quel est l'identifiant du destinataire ?\n")
         if ident >= len(utilisateurs) or ident==active_user.id or ident<0:
            input("Identifiant non valide\nAppuyez sur Entrée pour continuer")
         else:
            destinataire = utilisateurs[ident]
            montant = intInput("Quel est le montant de la transaction ?\n")
            if montant >= 0:
               tip = intInput("Combien donnez-vous en pourboire ?\n")
               if tip >= 0:
                  diffuserVirement(active_user.virement(destinataire,montant,tip,IDTRANSACTION.nextId()))
                  input("Transaction réussie\nAppuyez sur Entrée pour continuer")
               else:
                  input("Pourboire non valide\nAppuyez sur Entrée pour continuer")
            else:
               input("Montant non valide\nAppuyez sur Entrée pour continuer")
      elif j==3:
         active_user.construire_block(transactions,BLOCKCHAIN)
      elif j==4:
         active_user.voir_blocks()
         num_bloc = intInput("Quel bloc veux-tu miner ?\n")
         if num_bloc >= 0 and num_bloc < len(active_user.liste_blocks):
            active_user.valider_block(miner(active_user.liste_blocks[num_bloc]),utilisateurs,BLOCKCHAIN)
            print("Le bloc a été validé !")
            print(f"Vous avez gagné {get_total_tip(BLOCKCHAIN.lastBlock())+BLOCKCHAIN.halving}ϻ")
         else:
            print("Mauvais numéro de bloc")
         input("Appuyez sur Entrée pour continuer")
      elif j==5:
         print(BLOCKCHAIN)
         input("Appuyez sur Entrée pour continuer")
      elif j==6:
         input("Vous allez vous déconnecter\nAppuyez sur Entrée pour continuer")
      else:
         input("Veuillez faire un choix valide\nAppuyez sur Entrée pour continuer")

G = S32Point(Gx,Gy)
"""
e = 12
private = PrivateKey(e)
public = e*G
message = int.from_bytes(hash32(b'quoicoubeh'),'big')
sign = private.sign(message)
print(public.verify(message,sign))
"""
#initialisation
IDTRANSACTION = Id()
IDUTILISATEURS = Id()
BLOCKCHAIN = BlockChain()
transactions = []
utilisateurs = []
i=0
while i!=4:
   os.system('cls' if os.name == 'nt' else 'clear')
   i = intInput("Que souhaitez vous faire ?\n 1 - Nouvel utilisateur\n 2 - Se connecter\n 3 - Tout le monde mine\n 4 - Quitter\n")
   if i==1:
      pseudo = input("Comment vous appelez vous ?\n")
      ident = IDUTILISATEURS.nextId()
      utilisateurs.append(Miner(pseudo,ident))
      active_user = utilisateurs[ident]
      print(active_user)
      input("Appuyez sur Entrée pour continuer")
      session_utilisateur(active_user)
   elif i==2:
      ident = intInput("Quel est votre identifiant ?\n")
      if ident >= len(utilisateurs):
         print("Identifiant non valide")
      else:
         active_user = utilisateurs[ident]
         print(active_user)
      input("Appuyez sur Entrée pour continuer")
      session_utilisateur(active_user)
   elif i==3:
      lancer_minage_collectif(utilisateurs)
   elif i==4:
      input("Vous allez quitter la session... Aurevoir\nAppuyez sur Entrée pour quitter")
   else:
      input("Veuillez faire un choix valide\nAppuyez sur Entrée pour continuer")






"""
Julie = Miner("Julie",IDUTILISATEURS.nextId())
Bob = Miner("Bob",IDUTILISATEURS.nextId())
utilisateurs.append(Julie)
utilisateurs.append(Bob)
virement1 = Julie.virement(Bob,40,2,IDTRANSACTION.nextId())
diffuserVirement(virement1)

fraude = Transaction(Julie,Bob,40,2,IDTRANSACTION.nextId())
virement2 = (fraude,Bob.clePrivee.sign(fraude.getMessage()))

virement2 = Bob.virement(Julie,20,5,IDTRANSACTION.nextId())
diffuserVirement(virement2)
Bob.construire_block(transactions,BLOCKCHAIN)
proof = miner(Bob.liste_blocks[0])
Bob.valider_block(proof,utilisateurs,BLOCKCHAIN)
Bob.construire_block(transactions,BLOCKCHAIN)
proof1 = miner(Bob.liste_blocks[0])
Bob.valider_block(proof1,utilisateurs,BLOCKCHAIN)
print(BLOCKCHAIN)
"""