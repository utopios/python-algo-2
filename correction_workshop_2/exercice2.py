# Demander à l'utilisateur de saisir le niveau de gravité de l'incident
niveau_gravite = input("Veuillez entrer le niveau de gravité de l'incident (faible, modéré, élevé) : ")

# Utilisation de l'expression match pour classer l'incident et déterminer l'action à entreprendre
match niveau_gravite.lower():
    case "faible":
        action = "Enregistrer l'incident et le surveiller sans intervention immédiate."
    case "modéré":
        action = "Alerter l'équipe technique pour une évaluation."
    case "élevé":
        action = "Intervention d'urgence de l'équipe technique."
    case _:
        action = "Niveau de gravité inconnu. Veuillez saisir un niveau valide."

# Affichage de l'action à entreprendre
print(action)