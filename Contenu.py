class Content: 
    
    """Constructeur de la classe.
    La variable contentList contient tous les contenus possibles pour une fiole :"""
    def __init__(self):
        self.contentList = ["avancer", "reculer", "ortie", "poison"]

    """Permet de récupérer le contenu de la liste des contenus potentiels"""
    def getContents(self):
        return self.contentList