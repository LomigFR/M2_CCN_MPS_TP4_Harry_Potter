#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:20:50 2020

@author: guillaume_collet
"""

choixContenus = ["avancer", "reculer", ]


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
    
    # Les contenus des fioles 2 et 6 sont les mêmes => la fiole 2 ne peut donc pas contenir de poison :
    listeFioles[1].setPoison(False)

def traitementVinPoison(listeFioles):
    for bottle in listeFioles:

        
def traitement1et7(listeFiole):
    listeFiole[0]4

# Les contenus des fioles 2 et 6 sont les mêmes :
def traitement2egal6(listeFioles):
    if(listeFioles[1].getContenu() != ""):
        listeFioles[5].setContenu(listeFiole[1].getContenu())
    if(listeFioles[5].getContenu() != ""):
        listeFioles[1].setContenu(listeFiole[5].getContenu())

def traitement1egal7(listeFioles, contenu):
    for content in contenu.getContents:
        if(listeFioles[0].
