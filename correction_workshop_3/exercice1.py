# Initialisation des compteurs pour les serveurs actifs et inactifs
serveurs_actifs = 0
serveurs_inactifs = 0

# Boucle pour vérifier l'état de chaque serveur
# for i in range(1, 6):  # On commence à 1 pour rendre le comptage plus naturel pour l'utilisateur
#     # Demander à l'utilisateur l'état du serveur
#     etat_serveur = input(f"Entrez l'état du serveur {i} (actif/inactif) : ").lower()
    
#     # Incrémentation du compteur approprié en fonction de l'état du serveur
#     if etat_serveur == "actif":
#         serveurs_actifs += 1
#     elif etat_serveur == "inactif":
#         serveurs_inactifs += 1
#     else:
#         print("Entrée non valide, ce serveur sera considéré comme inactif.")
#         serveurs_inactifs += 1


## Avec une boucle while

serveur_numero = 1

while serveur_numero <= 5:
    etat_serveur = input(f"Entrez l'état du serveur {serveur_numero} (actif/inactif) : ").lower()
    if etat_serveur == "actif":
        serveurs_actifs += 1
    elif etat_serveur == "inactif":
        serveurs_inactifs += 1
    else:
        print("Entrée non valide, ce serveur sera considéré comme inactif.")
        serveurs_inactifs += 1
    
    serveur_numero += 1




print(f"Le nombre serveur actif {serveurs_actifs} et serveur inactif {serveurs_inactifs}")