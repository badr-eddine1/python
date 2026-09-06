produits = {
    "ordi" : 3500,
    "telephone" : 1500,
    "tablette" : 800,
    "chargeur" : 200
}
def menu():
    print("_____menu_____")
    print("1. afficher les produits disponibles")
    print("2. ajouté un produits au panier ")
    print("3. supprimer un produits du panier ")
    print("4. afficher panier ")
    print("5. calculer le total du panier ")
    print("6. quitter le programme ")

print("choisis une option du menu  :")
menu()
choix = input()
if choix == "1":
    print("produits disponibles :")
    for produit, prix in produits.items():
        print(f"{produit} : {prix} DH")
elif choix == "2":
    print("ajouter un produit au panier :")
    produit_choisi = input("nom du produit : ")
    if produit_choisi in produits:
        quantite = int(input("quantité : "))
        panier[produit_choisi] = quantite
        print(f"{quantite} {produit_choisi} ajouté au panier.")
    else:
        print("produit non disponible.")
elif choix == "3":
    print("supprimer un produit du panier :")
    produit_choisi = input("nom du produit : ")
    if produit_choisi in panier:
        del panier[produit_choisi]
        print(f"{produit_choisi} supprimé du panier.")
    else:
        print("produit non trouvé dans le panier.")
elif choix == "4":
    print("contenu du panier :")
    for produit, quantite in panier.items():
        print(f"{produit} : {quantite}")
elif choix == "5":
    total = 0
    for produit, quantite in panier.items():
        total += produits[produit] * quantite
    print(f"total du panier : {total} DH")
elif choix == "6":
    print("quitter le programme.")


