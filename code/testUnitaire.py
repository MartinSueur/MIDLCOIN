# -*- coding: utf-8 -*-

from classId import *
from class256Field import *
from class256Point import *
from constantes import *
from classPrivateKey import *
from classSignature import *
from classUser import *
from classMiner import *
from functions import *
from threading import *
from classThreadMiner import *
from classVerif import *
from heuristiques import *
import random


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




#initialisation
IDTRANSACTION = Id()
IDUTILISATEURS = Id()
BLOCKCHAIN = BlockChain()
transactions = []
utilisateurs = []


Julie = Miner("Julie",IDUTILISATEURS.nextId())
Bob = Miner("Bob",IDUTILISATEURS.nextId())
utilisateurs.append(Julie)
utilisateurs.append(Bob)
virement1 = Julie.virement(Bob,40,2,IDTRANSACTION.nextId())
diffuserVirement(transactions,virement1)

fraude = Transaction(Julie,Bob,40,2,IDTRANSACTION.nextId())
virement2 = (fraude,Bob.clePrivee.sign(fraude.getMessage()))

diffuserVirement(transactions,virement2)
Bob.construire_block(transactions,BLOCKCHAIN)