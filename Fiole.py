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
    
    def setContenu(self, valueContenu):
        self.contenu = valueContenu
    
    def getContenu(self):
        return self.contenu
    
    def getContenuChoix(self, content):
        tempContent = ""
        if(content == "poison"):
            tempContent = self.poison
        elif(content == "ortie"):
            tempContent = self.ortie
        elif(content == "avancer"):
            tempContent = self.avancer
        else(content == "reculer"):
            tempContent = self.reculer
        return tempContent