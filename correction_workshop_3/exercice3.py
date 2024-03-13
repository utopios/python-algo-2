# Initialisation des variables
avertissements_consecutifs = 0  # Compteur pour les avertissements consécutifs
seuil_latence = 100  # Seuil de latence en ms

# Boucle de surveillance continue
while True:
    # Demande à l'utilisateur de saisir la latence actuelle ou 'stop' pour arrêter
    saisie_utilisateur = input("Entrez la latence actuelle du réseau en ms ou 'stop' pour arrêter la surveillance : ")
    
    # Vérification si l'utilisateur souhaite arrêter la surveillance
    if saisie_utilisateur.lower() == 'stop':
        print("Arrêt de la surveillance du réseau.")
        break

    # Vérification si la saisie est un nombre
    if saisie_utilisateur.isdigit():
        latence_actuelle = int(saisie_utilisateur)
        if latence_actuelle > seuil_latence:
            print("Avertissement : la latence dépasse le seuil autorisé de 100 ms.")
            avertissements_consecutifs += 1  # Incrémentation du compteur d'avertissements
            action_corrective = input("Des actions correctives ont-elles été prises ? (oui/non) : ").lower()
            
            # Vérification si des actions correctives ont été prises
            if action_corrective == 'oui':
                avertissements_consecutifs = 0  # Réinitialisation du compteur d'avertissements
                print("Surveillance continue...")
            elif avertissements_consecutifs >= 3:
                print("Problème majeur détecté. Arrêt de la surveillance et nécessité d'une intervention immédiate.")
                break
        else:
            avertissements_consecutifs = 0  # Réinitialisation du compteur si la latence est en dessous du seuil
            print("La latence est dans les limites acceptables. Surveillance continue...")
    else:
        print("Veuillez entrer une valeur numérique pour la latence ou 'stop' pour arrêter la surveillance.")
