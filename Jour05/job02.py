def puissance(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return puissance(x * x, n // 2)
    else:
        return x * puissance(x * x, (n - 1) // 2)

x = int(input("Entrez un nombre entier x : "))
n = int(input("Entrez un nombre entier n : "))
resultat = puissance(x, n)
print(x, "2puissance", n, "est égal à", resultat)
