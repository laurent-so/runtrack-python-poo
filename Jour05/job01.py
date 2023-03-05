def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

nombre = int(input("Veuillez entrer un nombre entier quelconque : "))
resultat = factorielle(nombre)
print("La factorielle de", nombre, "est", resultat)
