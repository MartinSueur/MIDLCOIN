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

def thread_verification(liste_threads):
   termine = False
   while not termine :
      for threads in liste_threads :
         if threads.resultat > 0 :
            termine = True

   for threads in liste_threads :
      threads.termine = True

h_random = lambda x : random.randint(0,100000000)
h_increment = lambda x : x + 1


def lancer_minage_collectif(utilisateurs):
   liste_threads = []
   for i in range(len(utilisateurs)):
      if len(utilisateurs[i].liste_blocks) > 0 :
        if i < 50:
            liste_threads.append(ThreadMiner(utilisateurs[i],h_random))
        else:
            liste_threads.append(ThreadMiner(utilisateurs[i],h_increment))

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

for i in range(100):
    utilisateurs.append(Miner(f"user{i}",IDUTILISATEURS.nextId()))
    utilisateurs[i].liste_blocks.append(Block(0,utilisateurs[i]))
lancer_minage_collectif(utilisateurs)