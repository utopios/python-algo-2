reponse_utilisateur = input("Le serveur est-il en maintenance ? (oui/non) : ") == "oui"

message = "Serveur marche" if reponse_utilisateur == True else "Serveur en maintenance"

print(message)