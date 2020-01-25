#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:20:50 2020

@author: guillaume_collet
"""

def initialisation(listeFioles):
    # La potion 1 étant tout à gauche, elle ne peut être "précédée" par une
    # fiole de poison, donc son contenu ne peut être de l'ortie :
    listeFioles[0].setOrtie(False)
    
    # Ni la fiole 1 et ni la fiole 7 ne permet d'avancer :
    listeFioles[0].setAvancer(False)
    listeFioles[6].setAvancer(False)
    
    # Ni la fiole 3 ni la fiole 6 ne contient du poison :
    listeFioles[2].setPoison(False)
    listeFioles[5].setPoison(False)
    
    # Les contenus des fioles 2 et 6 sont les mêmes :
    listeFioles[1].set

def traitementVinPoison(listeFioles):
    for bottle in listeFioles:

        
def traitement1et7(listeFiole):
    listeFiole[0]4

def Traitement(listeFioles):
    
    