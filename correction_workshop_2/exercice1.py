# Demande à l'utilisateur la bande passante totale disponible
bande_passante_totale = float(input("Entrez la bande passante totale disponible dans le data center (en Gbps) : "))

# Pour simplifier, nous allons allouer la bande passante à un seul service pour cet exemple
priorite_service = int(input("Entrez la priorité du service (1-3, 1 étant le plus élevé) : "))
demande_bande_passante = float(input("Entrez la demande de bande passante pour le service (en Gbps) : "))

# Allocation simplifiée (tous les services ont la même priorité dans cet exemple)
# Vérification si la demande peut être totalement satisfaite
if demande_bande_passante <= bande_passante_totale:
    ### Avec La priorité
    match priorite_service:
        case 1:
            allocation = demande_bande_passante
        case 2:
            allocation = demande_bande_passante / 2
        case 3:
            allocation = demande_bande_passante / 3
        case _:
            allocation = 0
else:
    match priorite_service:
        case 1:
            allocation = bande_passante_totale
        case 2:
            allocation = bande_passante_totale / 2
        case 3:
            allocation = bande_passante_totale / 3
        case _:
            allocation = 0

# Affichage de l'allocation
print(f"Bande passante allouée au service : {allocation} Gbps.")
print(f"Bande passante à allouer : {bande_passante_totale - allocation} Gbps.")

# Notez que dans un scénario réel, vous auriez besoin de structures de données complexes et de boucles pour gérer plusieurs services.
