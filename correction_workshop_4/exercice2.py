# Initialisation de la liste pour stocker les informations des serveurs
liste_serveurs = []

# Boucle pour saisir les informations de plusieurs serveurs
while True:
    print("\nEntrez les informations du serveur. Tapez 'fin' pour terminer.")

    nom = input("Nom du serveur : ")
    if nom.lower() == 'fin':
        break

    ip = input("Adresse IP : ")
    type_serveur = input("Type de serveur (web, base de données, etc.) : ")
    etat = input("État (actif/inactif) : ")

    # Création d'un tuple pour le serveur actuel et ajout à la liste
    serveur = (nom, ip, type_serveur, etat)
    liste_serveurs.append(serveur)

# Parcourir la liste des serveurs pour afficher leurs informations
print("\nInformations sur les serveurs :")
for serveur in liste_serveurs:
    nom, ip, type_serveur, etat = serveur
    print(f"Nom: {nom}, IP: {ip}, Type: {type_serveur}, État: {etat}")
