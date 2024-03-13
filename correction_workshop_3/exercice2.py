# Initialisation du compteur pour les unités nécessitant une inspection manuelle
unites_inspection_manuelle = 0

# Boucle pour simuler la vérification de chaque unité de stockage
for unite in range(1, 4):  # Simule la vérification de 3 unités de stockage
    tentatives = 0  # Initialisation du compteur de tentatives pour l'unité actuelle
    
    # Boucle de tentatives de test pour l'unité de stockage
    while tentatives < 3:
        # Demander à l'utilisateur le résultat du test
        resultat_test = input(f"Le test de l'unité de stockage {unite} a-t-il réussi ? (oui/non) : ").lower()
        
        # Vérification du résultat du test
        if resultat_test == "oui":
            print(f"L'unité de stockage {unite} a passé le test avec succès.")
            break  # Sortie de la boucle si le test est réussi
        else:
            tentatives += 1  # Incrémentation du compteur de tentatives
            if tentatives < 3:
                print(f"Tentative {tentatives} échouée. Retenter le test...")
    
    # Vérifier si l'unité nécessite une inspection manuelle
    if tentatives == 3:
        print(f"L'unité de stockage {unite} nécessite une inspection manuelle.")
        unites_inspection_manuelle += 1

# Affichage du nombre d'unités nécessitant une inspection manuelle
print(f"Nombre d'unités nécessitant une inspection manuelle : {unites_inspection_manuelle}")
