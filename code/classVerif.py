from threading import *
from classMiner import *

class ThreadVerif(Thread):
    """
    Thread arrêtant tous les processus de minage quand un mineur valide un bloc
    """
    def __init__(self, liste_threads):
        Thread.__init__(self)
        self.liste_threads = liste_threads
        self.thread_gagnant = None
    #processus de vérification d'arrêt d'un thread de minage
    def run(self):
        termine = False
        lock = RLock()
        while not termine and len(self.liste_threads) > 0:
            for threads in self.liste_threads :
                if threads.resultat > 0 :
                    termine = True
                    self.thread_gagnant = threads

        with lock :
            for threads in self.liste_threads :
                threads.termine = True

        