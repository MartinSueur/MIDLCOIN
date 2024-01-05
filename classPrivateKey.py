from constantes import *
from classSignature import *
from hashlib import sha256
from class32Point import *
from random import randint
import hmac

G = S32Point(Gx,Gy)

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G
    def hex(self):
        return '{:x}'.format(self.secret).zfill(8)
    def sign(self, z):
        k = self.random_k()
        r = (k * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N / 2:
            s = N - s
        return Signature(r, s)
    
    def get_int(zh,N):
        qlen = N.bit_length()//8
        if(len(zh) > qlen):
            zh = zh[:(qlen)]

        z = int.from_bytes(zh,byteorder='big')%N
        return z

    def deterministic_k(self, z):
        SIZE = N.bit_length()//8
        k = b'\x00' * SIZE
        v = b'\x01' * SIZE
        if z > N:
            z -= N
        z_bytes = z.to_bytes(SIZE, 'big')
        e_bytes = self.e.to_bytes(SIZE, 'big')
        s256 = self.h
        #double hash sha256 pour obtenir un k,v aléatoire
        k = hmac.new(k, v + b'\x00' + e_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + e_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        trouve = False
        while (not trouve):
            v = hmac.new(k, v, s256).digest()
            candidat = self.get_int(v,N)
            if candidat >= 1 and candidat < self.PREMIER:
                return candidat
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
    
    def deterministic_k2(self, z):
        k = b'\x00' * 4
        v = b'\x01' * 4
        if z > N:
            z -= N
        z_bytes = z.to_bytes(4, 'big')
        secret_bytes = self.secret.to_bytes(4, 'big')
        s32 = sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s32).digest()[:4]
        v = hmac.new(k, v, s32).digest()[:4]
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s32).digest()[:4]
        v = hmac.new(k, v, s32).digest()[:4]
        while True:
            v = hmac.new(k, v, s32).digest()[:4]
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s32).digest()[:4]
            v = hmac.new(k, v, s32).digest()[:4]
    def random_k(self):
        return randint(1,N-1)
