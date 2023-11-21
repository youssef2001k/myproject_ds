




class Livre:
    def __init__(self , titre , auteur , prix , nbpages):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.nbpages = nbpages
        self.proprietaire = None
        
    def __str__(self):
        if self.proprietaire == None:
            res = " // Livre neuf"
        else:
            res = "  // Propriétaire : " + self.proprietaire
            
        return "Titre : " + self.titre + "  // Auteur : " + self.auteur + " // Prix : " + str(self.prix) + " // Propriétaire : " + res
    
    def acheter(self , proprietaire):
        if self.proprietaire == None:
            self.proprietaire = proprietaire
        else :
            print("Livre déjà vendu")



hp = Livre("Harry Potter", "J. K. Rowling", 79.9, 350)
print(hp)
print()
hp.acheter("Hatem")
hp.acheter("Fatma")
print(hp)
print()
tintin1 = BD("Tintin en Amérique", "Hergé", 40.0, 80, enCouleur=True)
tintin2 = BD("Tintin au Congo", "Hergé", 40.0, 80, enCouleur=True)
tintin1.echanger(tintin2)
print()
print(tintin2)
print()
bibrsi2 = BibDeClasse()
bibrsi2.ajouter(tintin1)
bibrsi2.ajouter(tintin2)
bibrsi2.ajouter(hp)
bibrsi2.ajouter(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.ajouter(tintin1)
print()
bibrsi2.afficher()

 
