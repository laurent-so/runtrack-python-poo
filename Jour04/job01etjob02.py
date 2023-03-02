class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("l'âge de la personne est:", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")


p = Personne()
p.afficherAge()  

e = Eleve()
e.affichageAge()  

# Instanciation d'un objet Eleve
e = Eleve()

# Faire dire bonjour à l'élève
e.bonjour()

# Envoyer l'élève en cours
e.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
e.modifierAge(15)

# Instanciation d'un objet Professeur
p = Professeur("Mathématiques")

# Faire dire bonjour au professeur
p.bonjour()

# Commencer le cours
p.enseigner()
