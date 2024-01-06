import random 

"""
Dans ce fichier on définit les heuristiques de minages qui pourront être utilisées, c'est à dire la manière dont on cherche la proof of work
"""


#on prend des entiers aléatoires entre 0 et 100000000
def h_random(x):
	return random.randint(0,100000000)

#on prend les entiers dans l'ordre croissant
def h_increment(x):
	return x+1