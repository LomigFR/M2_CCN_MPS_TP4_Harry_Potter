#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:20:50 2020

@author: guillaume_collet
"""

class Bottle: 
    
    # Les variables attributs poison, soupe, reculer et avancer sont des booléens.
    # id est un entier
    
    def __init__(self, id):
        self.id = id
        self.contenu = ""
        self.poison = None
        self.ortie = None
        self.reculer = None
        self.avancer = None
    
    def setPoison(self, valuePoison):
        self.poison = valuePoison

    def getPoison(self):
        return self.poison
    
    def setOrtie(self, valueOrtie):
        self.ortie = valueOrtie

    def getOrtie(self):
        return self.ortie
    
    def setReculer(self, valueReculer):
        self.reculer = valueReculer

    def getReculer(self):
        return self.reculer
    
    def setAvancer(self, valueAvancer):
        self.avancer = valueAvancer

    def getAvancer(self):
        return self.avancer
    
    def getId(self):
        return self.id
    
    def setContenu(self):
        if(self.poison):
            contenu = "Poison"
        elif(self.ortie):
            contenu = "Ortie"
        elif(self.reculer):
            contenu = "Reculer"
        else:
            contenu = "Avancer"
    
    def getContenu(self):
        return self.contenu