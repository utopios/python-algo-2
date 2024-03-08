# Demande à l'utilisateur la capacité des batteries de secours et la consommation moyenne
capacite_batteries = float(input("Entrez la capacité totale des batteries de secours (en kWh) : "))
consommation_moyenne = float(input("Entrez la consommation énergétique moyenne du data center par heure (en kW) : "))

# Calcul du temps de fonctionnement restant
temps_fonctionnement_total = capacite_batteries / consommation_moyenne
temps_fonctionnement_heures = int(temps_fonctionnement_total)
temps_fonctionnement_minutes= int((temps_fonctionnement_total - temps_fonctionnement_heures) * 60) 
# Affichage du temps de fonctionnement restant
print(f"Le data center peut continuer à fonctionner pendant {temps_fonctionnement_heures} heures, {temps_fonctionnement_minutes} minutes en utilisant uniquement les batteries de secours.")
