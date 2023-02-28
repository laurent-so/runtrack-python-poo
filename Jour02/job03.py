class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  
    
    def get_titre(self):
        return self.__titre

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté auparavant.")

            
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(livre1.verification())   
livre1.emprunter()   
print(livre1.verification())   
livre1.emprunter()  
livre1.rendre()   
print(livre1.verification())   
livre1.rendre()   
