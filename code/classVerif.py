from threading import *
from classMiner import *
from functions import *

class ThreadVerif(Thread):
    def __init__(self, liste_threads):
        Thread.__init__(self)
        self.liste_threads = liste_threads
        self.thread_gagnant = None

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

        