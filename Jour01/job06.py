class Animal:

    def __init__(self):
        self.age = 3
        self.nom = ""

    
    def vieillir(self):
        self.age += 1

    
    def nommer(self, nouveau_nom):
        self.nom = nouveau_nom
        

mon_animal = Animal()
print("Âge animal :", mon_animal.age)

mon_animal.vieillir()
print("Âge l'année suivante :", mon_animal.age)

mon_animal.nommer("LuNaaaa")
print("L'animal s'appelle", mon_animal.nom)