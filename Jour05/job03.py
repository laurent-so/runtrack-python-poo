def longueur(chaîne):
    if chaîne == "":
        return 0
    else:
        return 1 + longueur(chaîne[1:])

chaîne = input("Entrez une chaîne de caractères : ")
resultat = longueur(chaîne)
print("La longueur de la chaîne", chaîne, "est", resultat)
