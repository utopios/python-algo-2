# Demande à l'utilisateur le coût par kWh, la consommation du système de refroidissement et le nombre d'heures de fonctionnement
cout_par_kWh = float(input("Entrez le coût par kWh : "))
consommation_refroidissement_par_heure = float(input("Entrez la consommation énergétique du système de refroidissement par heure (en kW) : "))
heures_fonctionnement_refroidissement = float(input("Combien d'heures le système de refroidissement a-t-il fonctionné aujourd'hui ? "))

# Calcul du coût total du refroidissement
cout_total_refroidissement = cout_par_kWh * consommation_refroidissement_par_heure * heures_fonctionnement_refroidissement

# Affichage du coût total
print(f"Le coût total du refroidissement pour la journée est de {cout_total_refroidissement:0.2f} euros.")