# Demander à l'utilisateur le nombre total de ressources disponibles
ressources_disponibles = int(input("Entrez le nombre total de ressources disponibles : "))

# Demander le nombre de ressources demandées par le processus
ressources_demandees = int(input("Entrez le nombre de ressources demandées par le processus : "))

# Utilisation de l'opérateur ternaire pour décider de l'allocation
allocation = "Demande acceptée. Les ressources sont allouées." if ressources_demandees <= ressources_disponibles else "Demande refusée. Ressources insuffisantes."

# Affichage du résultat de l'allocation
print(allocation)