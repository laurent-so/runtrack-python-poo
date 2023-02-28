class Student:
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def get_credits(self):
        return self.__credits
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
    
    def studentInfo(self):
        print("nom =", self.__nom, "prénom =", self.__prenom, "id =", self.__id, "Niveau =", self.__level)

etudiant1 = Student("Doe", "John", 145)
etudiant1.add_credits(10)
etudiant1.add_credits(20)
etudiant1.add_credits(0) # cette opération n'affectera pas le total de crédits
print("Le nombre de crédits de", etudiant1.get_prenom(), etudiant1.get_nom(), "est de", etudiant1.get_credits(), "points")

    
john_doe = Student("Doe", "John", 145)
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(50)
john_doe.studentInfo()
