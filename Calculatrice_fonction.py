"""
Nom : Calculatrice_fonction.py
Auteur : Gendroz Gaetan
Date : 11.11.2024
"""

def choix_de_nombre():
    nb1 = int(input("Chiffre 1 : "))
    nb2 = int(input("Chiffre 2 : "))

    return nb1
    return nb2


def addition():
    print("La somme vaut : ", nb1 + nb2)


def soustraction():
    print("La différence vaut : ", nb1 - nb2)


def multiplication():
    print("Le produit vaut : ", nb1 * nb2)


def division():
    print("Le quotient vaut : ", nb1 // nb2)


def calcule():

    while True:
        choix = input("Quelle opération voulez-vous faire avec ces nombres? Choisissez parmis: addition, soustraction, multiplication, division ou rien. ")

        if choix == "addition":
            addition()

        elif choix == "soustraction":
            soustraction()

        elif choix == "multiplication":
            multiplication()
        elif choix == "division":
            division()
        elif choix == "rien":
            break
        else:
            print("Le choix n'est pas valide.")

choix_de_nombre()
calcule()

