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
from classThreadMiner import *
from classVerif import *
from heuristiques import *
import time

def str_temps(secondes):
   chaine = ""
   minutes = 0
   heures = 0
   while secondes > 60 :
      minutes += 1
      secondes -= 60
   while minutes > 60 :
      heures += 1
      minutes -= 60
   if heures != 0 :
      chaine += f"{heures} heures "
   if minutes != 0 :
      chaine += f"{minutes} minutes "
   if secondes != 0 :
      chaine += f"{round(secondes,3)} secondes "
   return chaine

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
   total = 0
   get_total_tip= 0
   for trans in block.transactions:
      total+=trans.tip
   return total


def lancer_minage_collectif(utilisateurs):
   liste_threads = []
   for i in range(len(utilisateurs)):
      if len(utilisateurs[i].liste_blocks) > 0 :
            liste_threads.append(ThreadMiner(utilisateurs[i],h_random))

   verif = ThreadVerif(liste_threads)

   verif.start()

   debut = time.time()

   for threads in liste_threads :
      threads.start()

   verif.join()
      
   for threads in liste_threads :
      threads.join()

   tempstotal = time.time() - debut
   if len(liste_threads) > 0 :
      print(f"Le mineur le plus rapide est : {verif.thread_gagnant.mineur.pseudo}")
      verif.thread_gagnant.mineur.valider_block(verif.thread_gagnant.resultat, utilisateurs, BLOCKCHAIN)
      print(f"Le bloc a été validé en {str_temps(tempstotal)} !")
      input("Appuyez pour continuer...")
   else :
      print("Aucun mineur n'a de bloc à miner.")
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
            debut = time.time()
            active_user.valider_block(miner(active_user.liste_blocks[num_bloc]),utilisateurs,BLOCKCHAIN)
            tempstotal = time.time() - debut
            print(f"Le bloc a été validé en {str_temps(tempstotal)} !")
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

"""
G = S32Point(Gx,Gy)
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