class Launch:

    """Constructeur de la classe :"""
    def __init__(self, listeFioles, contenus):
        self.listeFioles = listeFioles
        self.contenus = contenus

    """Lance l'exécution de la séquence des méthodes relatives au traitement de l'énigme :"""
    def run(self):
        while(self.decompteTrue(self.listeFioles) != 7):
            self.init()
            self.traitement2egale6(self.listeFioles)
            self.traitement1different7(self.listeFioles, self.contenus)
            self.traitementPoisonVsOrtie(self.listeFioles)
            self.eliminationOrtie(self.listeFioles)
            self.deductionFalseByTrue(self.listeFioles)
            self.deductionTrueByFalse(self.listeFioles)
            self.ecritureContenuFinal(self.listeFioles)

    """Permet d'effectuer les réglages de certains états de contenus potentiels en fonction de l'énoncé de l'énigme :"""
    def init(self):
        """Ni la fiole 3 ni la fiole 6 ne contient du poison :"""
        self.listeFioles[2].setPoison(False)
        self.listeFioles[5].setPoison(False)
    
    """Les contenus des fioles 2 et 6 sont les mêmes. On en déduit que :
         => la fiole 2 ne peut donc pas contenir de poison (puisque la 6 n'en contient pas)
         => ni l'une ni l'autre ne peut contenir la potion avancer ou reculer car ces potions ne sont présentes qu'en un 
         seul exemplaire chacune. Conclusion : les fioles 2 et 6 contiennent nécessairement de l'ortie."""
    def traitement2egale6(self, listeFioles):
        listeFioles[5].setAvancer(False)
        listeFioles[5].setReculer(False)
        listeFioles[1].setAvancer(False)
        listeFioles[1].setReculer(False)
        listeFioles[1].setPoison(False)
        listeFioles[1].setOrtie(True)
        listeFioles[5].setOrtie(True)

    """Ni la fiole 1 et ni la fiole 7 ne permet d'avancer. Par ailleurs, ces deux fioles ont des contenus différents :"""
    def traitement1different7(self, listeFioles, contenu):
        listeFioles[0].setAvancer(False)
        listeFioles[6].setAvancer(False)
        for content in contenu.getContents:
            if(listeFioles[0].getContenuChoix(content) == True):
                listeFioles[6].setContenuChoix(content) == False
            if(listeFioles[6].getContenuChoix(content) == True):
                listeFioles[0].setContenuChoix(content) == False

    """A gauche d'une fiole de vin d'ortie doit se trouver une fiole de poison. On en déduit que :
       - la potion 1 étant tout à gauche, elle ne peut être précédée d'une fiole de poison, 
       donc son contenu ne peut être de l'ortie
       - la potion 7 étant tout à droite, elle ne peut être suivie d'une fiole d'ortie, 
       donc son contenu ne peut être du poison"""
    def traitementPoisonVsOrtie(self, listeFioles):
        listeFioles[0].setOrtie(False)
        listeFioles[6].setPoison(False)
        for i in range(7):
            if(i>=1 & i<6):
                if(listeFioles[i].getOrtie()):
                    listeFioles[i-1].setPoison(True)
                if(listeFioles[i].getPoison() == False):
                    listeFioles[i+1].setOrtie(False)

    """Décompte du nombre de fioles contenant du vin d'ortie :"""
    def decompteOrtie(self, listeFioles):
        temp = 0
        for bottle in listeFioles:
            if(bottle.getOrtie()):
                temp += 1
        return temp

    """Mettre les contenus d'ortie à false pour toutes les autres fioles une fois qu'on a trouvé les 2 qui en contiennent :"""
    def eliminationOrtie(self, listeFioles):
        if(self.decompteOrtie(listeFioles) == 2):
            for bottle in listeFioles:
                if(bottle.getOrtie() != True):
                    bottle.setOrtie(False)

    """Parce qu'il y a 1 true dans les contenus potentiels d'une fiole, les 3 autres sont obligatoirement à false."""
    def deductionFalseByTrue(self, listeFioles):
        for bottle in listeFioles:
            for i in range(4):
                if(bottle.getListeContenu()[i] != True):
                    bottle.getListeContenu()[i] = False

    """Parce qu'il y a 3 false dans les contenus potentiels d'une fiole, le 4ème contenu est obligatoirement à true :"""
    def deductionTrueByFalse(self, listeFioles):
        for bottle in listeFioles:
            if(self.decompteFalse(bottle) == 3):
                for i in range(4):
                    if(bottle.getListeContenu()[i] != False):
                        bottle.getListeContenu()[i] = True

    """Ecriture de la variable String contenuFinal d'une fiole :"""
    def ecritureContenuFinal(self, listeFioles):
        for bottle in self.listeFiole:
            if(bottle.getOrtie()):
                bottle.setContenuFinal("ortie")
            elif(bottle.getPoison()):
                bottle.setContenuFinal("poison")
            elif(bottle.getAvancer()):
                bottle.setContenuFinal("avancer")
            else:
                bottle.setContenuFinal("reculer")

    """Décompte du nombre de contenus à false pour une fiole :"""
    def decompteFalse(self, bottle):
        temp = 0
        for content in bottle.getListeContenu():
            if(content):
                temp += 1
        return temp

    """Décompte des contenus à True pour l'ensemble des fioles :"""
    def decompteTrue(self, listeFioles):
        temp = 0
        for bottle in listeFioles:
            for content in bottle.getListeContenu():
                if(content):
                    temp += 1
        return temp