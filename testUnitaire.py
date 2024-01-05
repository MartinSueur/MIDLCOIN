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
import random

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


def lancer_minage_collectif(utilisateurs):
   liste_threads = []
   for i in range(len(utilisateurs)):
      if len(utilisateurs[i].liste_blocks) > 0 :
            liste_threads.append(ThreadMiner(utilisateurs[i],h_random))

   verif = ThreadVerif(liste_threads)

   verif.start()

   for threads in liste_threads :
      threads.start()

   verif.join()   
      
   for threads in liste_threads :
      threads.join()

   print(f"Le mineur le plus rapide est : {verif.thread_gagnant.mineur.pseudo}")
   verif.thread_gagnant.mineur.valider_block(verif.thread_gagnant.resultat, utilisateurs, BLOCKCHAIN)
   print("Le bloc a été validé")
   input("Appuyez pour continuer...")



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

for i in range(100):
    utilisateurs.append(Miner(f"user{i}",IDUTILISATEURS.nextId()))
    utilisateurs[i].liste_blocks.append(Block(0,utilisateurs[i]))
lancer_minage_collectif(utilisateurs)