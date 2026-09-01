liste = []

while True:

    print("\n----- MENU -----")
    print("1. Ajouter un nombre")
    print("2. Supprimer un nombre")
    print("3. Afficher la liste")
    print("4. Afficher le plus grand nombre")
    print("5. Afficher le plus petit nombre")
    print("6. Calculer la moyenne")
    print("7. Rechercher un nombre")
    print("8. Quitter")

    choix = int(input("Choisissez une option : "))

    # Ajouter
    if choix == 1:
        nombre = float(input("Entrez un nombre : "))
        liste.append(nombre)
        print("Nombre ajouté avec succès !")

    # Supprimer
    elif choix == 2:
        nombre = float(input("Entrez le nombre à supprimer : "))

        if nombre in liste:
            liste.remove(nombre)
            print("Nombre supprimé avec succès !")
        else:
            print("Nombre introuvable.")

    # Afficher
    elif choix == 3:
        print("Liste actuelle :", liste)

    # Maximum
    elif choix == 4:
        if len(liste) > 0:
            print("Le plus grand nombre est :", max(liste))
        else:
            print("La liste est vide.")

    # Minimum
    elif choix == 5:
        if len(liste) > 0:
            print("Le plus petit nombre est :", min(liste))
        else:
            print("La liste est vide.")

    # Moyenne
    elif choix == 6:
        if len(liste) > 0:
            moyenne = sum(liste) / len(liste)
            print("La moyenne est :", moyenne)
        else:
            print("La liste est vide.")

    # Rechercher
    elif choix == 7:
        nombre = float(input("Entrez le nombre à rechercher : "))

        if nombre in liste:
            print("Le nombre existe dans la liste.")
        else:
            print("Le nombre n'existe pas dans la liste.")

    # Quitter
    elif choix == 8:
        print("Au revoir !")
        break

    # Choix invalide
    else:
        print("Choix invalide.")