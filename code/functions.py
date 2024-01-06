from class256Point import *
from hashlib import sha256
from math import sqrt
from constantes import DIFFICULTEMINAGE

"""
Ce sont les petites fonctions dont nous avons eu besoin mais qui n'appartiennent a aucune classe,
elles nous ont servies pour factoriser le code
"""

#affiche la liste des transactions
def voir_transactions(transactions):
    for trans in transactions:
        print(trans)
#permet de trouver une transaction avec son identifiant
def find_trans_by_id(transactions,id):
    for trans in transactions:
        if trans.id == id:
            return trans
    return -1
#la condition de validation d'un hash : il doit finir par 54321 si n=5 (cas général : n n-1 n-2 ... 2 1)
def condition_hash_valide(strHash,n=DIFFICULTEMINAGE):
    res = True
    for i in range(n):
        if strHash[256-i-1] != str(i+1):
           res = False
    return res
#deux tours de sha256 pour plus de sécurité
def hash256(s):
    return sha256(sha256(s).digest()).digest()
#ordre d'un point d'une courbe elliptique
def ordre(g):
    res = 1
    g_de_base = g
    while g != S256Point(None,None):
        g += g_de_base
        res+=1
    return res
#est-ce que n est premier
def is_prime(n):
  for i in range(2,int(sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True
#permet de réaliser un int(input()) en vérifiant que le résultat entré est bien un entier
def intInput(chaine):
    i = input(chaine)
    if i.isdigit():
        return int(i)
    return -1
#affichage d'une durée
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
#vérifie la signature d'un virement et publie la transaction si elle est valide
def diffuserVirement(transactions,virement): # un virement est un couple transaction,signature
    trans = virement[0]
    sign = virement[1]
    if trans.emetteur.clePublique.verify(trans.getMessage(),sign):
        transactions.append(trans)
#affiche un utilisateur
def voir_user(user):
    print(f"Utilisateur n°{user.id} : {user.pseudo}")
#afficher le registre des utilisateurs
def voir_registre_users(users):
    for user in users:
      voir_user(user)
#permet d'afficher un nombre en base10 sur 256bits
def format256(hash):
    return f'{hash:256d}'