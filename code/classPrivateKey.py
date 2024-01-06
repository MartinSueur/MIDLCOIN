from constantes import *
from classSignature import *
from hashlib import sha256
from class256Point import *
import random
import hmac

G = S256Point(Gx,Gy)

class PrivateKey:
    """
    Classe représentant la clé privée d'un utilisateur générée par un nombre secret
    """
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G
    #représenter en hexa sur 256bits
    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)
    #permet de signer un message avec sa clé privée
    def sign(self, z):
        #k = self.deterministic_k(z)
        k = self.random_k()
        r = (k * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N / 2:
            s = N - s
        return Signature(r, s)
    #permet de trouver un k pour la signature
    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
    def random_k(self):
        return random.randint(1,N)