utilisateurs = {}

def ajouter_utilisateur(nom, role):
    utilisateurs[nom] = role
    print(f"Utilisateur {nom} ajouté avec le rôle {role}.")

def changer_role(nom, nouveau_role):
    if nom in utilisateurs.keys():
        utilisateurs[nom] = nouveau_role
        print(f"Rôle de l'utilisateur {nom} changé en {nouveau_role}.")
    else:
        print(f"L'utilisateur {nom} n'existe pas.")

def afficher_utilisateurs():
    for nom, role in utilisateurs.items():
        print(f"Nom: {nom}, Rôle: {role}")

# Exemple d'utilisation
ajouter_utilisateur("Alice", "Administrateur")
ajouter_utilisateur("Bob", "Opérateur")
afficher_utilisateurs()
changer_role("Alice", "Opérateur")
changer_role("Bob", "Administrateur")
changer_role("Toto", "Administrateur")
afficher_utilisateurs()
