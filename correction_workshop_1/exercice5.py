reponse_utilisateur = input("Le serveur est-il en maintenance ? (oui/non) : ") == "oui"

message = "En etat" if reponse_utilisateur else "En maintenance"

print(message)