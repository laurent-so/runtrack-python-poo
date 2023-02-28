class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

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

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)

print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nb_pages()) 


livre1.set_titre("Le Grand Prince")
print(livre1.get_titre())   
livre1.set_auteur("Laurent")
print(livre1.get_auteur())  
livre1.set_nb_pages(150)
print(livre1.get_nb_pages())   
