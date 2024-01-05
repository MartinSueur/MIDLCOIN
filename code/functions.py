from class32Point import *
from hashlib import sha256
from math import sqrt
from constantes import DIFFICULTEMINAGE
import time

def find_trans_by_id(transactions,id):
    for trans in transactions:
        if trans.id == id:
            return trans
    return -1

def condition_hash_valide(strHash,n=DIFFICULTEMINAGE):
    res = True
    for i in range(n):
        if strHash[32-i-1] != str(i+1):
           res = False
    return res

def hash32(s):
    '''two rounds of sha32'''
    return sha256(sha256(s).digest()).digest()[:4]

def ordre(g):
    res = 1
    g_de_base = g
    while g != S32Point(None,None):
        g += g_de_base
        res+=1
    return res

def is_prime(n):
  for i in range(2,int(sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def intInput(chaine):
    i = input(chaine)
    if i.isdigit():
        return int(i)
    return -1

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

def diffuserVirement(transactions,virement): # un virement est un couple transaction,signature
   trans = virement[0]
   sign = virement[1]
   #if trans.emetteur.clePublique.verify(trans.getMessage(),sign):
   transactions.append(trans)

def voir_user(user):
   print(f"Utilisateur n°{user.id} : {user.pseudo}")

def voir_registre_users(users):
   for user in users:
      voir_user(user)

def format32(hash):
    return f'{hash:32d}'