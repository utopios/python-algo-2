# Demande à l'utilisateur la consommation moyenne par heure et le nombre d'heures de fonctionnement
consommation_par_heure = float(input("Entrez la consommation énergétique moyenne du data center par heure (en kW) : "))
heures_fonctionnement = float(input("Combien d'heures le data center a-t-il fonctionné aujourd'hui ? "))

# Calcul de la consommation énergétique totale
consommation_totale = consommation_par_heure * heures_fonctionnement

# Affichage du résultat
print(f"La consommation énergétique totale de la journée est de {consommation_totale:0.2f} kW.")