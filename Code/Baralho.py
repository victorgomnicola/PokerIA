# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:27 2019

@author: victo
"""
from random import shuffle

class Baralho:
    
    def __init__(self):
        self.cartas = []
        
    def iniciarBaralho(self):
        self.cartas = []
        for i in range(1,14):
            for j in ['o', 'e', 'c', 'p']:
                self.cartas.append(str(i) + j)

        self.embaralhar()
                              
    def embaralhar(self):
        shuffle(self.cartas)
        
    def tirarCarta(self):
        return self.cartas.pop()
    
    