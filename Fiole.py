class Bottle: 
    
    """Les variables attributs poison, ortie, reculer et avancer sont des booléens.
       La variable id est un entier :"""
    def __init__(self):
        self.contenuFinal = ""
        self.poison = None
        self.ortie = None
        self.reculer = None
        self.avancer = None
        self.listeContenu = [self.poison, self.ortie, self.avancer, self.reculer]
    
    """Permet de récupérer la liste des états des contenus potentiels d'une fiole :"""
    def getListeContenu(self):
        return self.listeContenu
    
    """Permet d'ajuster la valeur de l'état du contenu potentiel "poison" en fonction d'une valeur imposée en paramètre :"""
    def setPoison(self, valuePoison):
        self.poison = valuePoison

    """Permet de récupérer l'état du contenu potentiel "poison" d'une fiole :"""
    def getPoison(self):
        return self.poison
    
    """Permet d'ajuster la valeur de l'état du contenu potentiel "ortie" en fonction d'une valeur imposée en paramètre :"""
    def setOrtie(self, valueOrtie):
        self.ortie = valueOrtie

    """Permet de récupérer l'état du contenu potentiel "ortie" d'une fiole :"""
    def getOrtie(self):
        return self.ortie
    
    """Permet d'ajuster la valeur de l'état du contenu potentiel "reculer" en fonction d'une valeur imposée en paramètre :"""
    def setReculer(self, valueReculer):
        self.reculer = valueReculer
        
    """Permet de récupérer l'état du contenu potentiel "reculer" d'une fiole :"""
    def getReculer(self):
        return self.reculer
    
    """Permet d'ajuster la valeur de l'état du contenu potentiel "avancer" en fonction d'une valeur imposée en paramètre :"""
    def setAvancer(self, valueAvancer):
        self.avancer = valueAvancer
    
    """Permet de récupérer l'état du contenu potentiel "avancer" d'une fiole :"""
    def getAvancer(self):
        return self.avancer
    
    """Permet d'affecter une valeur imposée en paramètre à la variable String contenuFinal :"""
    def setContenuFinal(self, valueContenu):
        self.contenuFinal = valueContenu
    
    """Permet de récupérer le contenu de la variable String décrivant le contenu de la fiole :"""
    def getContenuFinal(self):
        return self.contenuFinal
    
    """Permet de récupérer une valeur de contenu relativement à une liste de choix disponible dans la classe Content :"""
    def getContenuChoix(self, content):
        tempContent = ""
        if(content == "poison"):
            tempContent = self.poison
        elif(content == "ortie"):
            tempContent = self.ortie
        elif(content == "avancer"):
            tempContent = self.avancer
        else:
            tempContent = self.reculer
        return tempContent
    
    """Permet de faire basculer un état de contenu potentiel d'une fiole à true en fonction d'un choix imposé en paramètre :"""
    def setContenuChoix(self, content):
        if(content == "poison"):
            self.setPoison(True)
        elif(content == "ortie"):
            self.setOrtie(True)
        elif(content == "avancer"):
            self.setAvancer(True)
        else:
            self.setReculer(True)