class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def périmetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        

class Parallelepipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

r = Rectangle(5, 3) 
print("Périmètre : ", r.périmetre())
print("Surface : ", r.surface())
r.set_longueur(8)
r.set_largeur(7)
print("Périmètre : ", r.périmetre())
print("Surface : ", r.surface())

p = Parallelepipède(4, 7, 8)
print("Périmètre : ", p.périmetre())
print("Surface : ", p.surface())
print("Volume : ", p.volume()) 
p.set_hauteur(9)
print("Volume : ", p.volume())
