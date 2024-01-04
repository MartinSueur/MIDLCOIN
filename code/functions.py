from class32Point import *
from hashlib import sha256
from math import sqrt

def find_trans_by_id(transactions,id):
    for trans in transactions:
        if trans.id == id:
            return trans
    return -1

def format32(hash):
    return f'{hash:32d}'

def condition_hash_valide(strHash,n=6):
    res = True
    for i in range(n):
        if strHash[32-i-1] != str(i+1):
           res = False
    return res

def miner(block):
    strHash = format32(block.get_hash())
    while not condition_hash_valide(strHash):
        block.proof += 1
        strHash = format32(block.get_hash())
        #print(f"{block.proof} : {strHash}")
    return block.proof

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