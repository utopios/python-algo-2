# Initialisation de la liste des tâches de maintenance
taches_maintenance = []

# Demander à l'utilisateur de saisir des tâches jusqu'à ce qu'il entre 'fin'
while True:
    tache = input("Entrez une tâche de maintenance prévue pour la journée (tapez 'fin' pour terminer) : ")
    if tache.lower() == 'fin':
        break
    taches_maintenance.append(tache)

# Affichage de la liste complète des tâches
print("\nListe complète des tâches de maintenance :")
for tache in taches_maintenance:
    print(f"- {tache}")

# Simuler l'exécution de chaque tâche
while len(taches_maintenance) > 0:
#while taches_maintenance:
    # Supposer que la première tâche de la liste est exécutée
    tache_en_cours = taches_maintenance.pop(0)
    print(f"\nExécution de la tâche : {tache_en_cours}")
    
    # Affichage de la liste mise à jour des tâches restantes
    if taches_maintenance:
        print("Tâches restantes :")
        for tache in taches_maintenance:
            print(f"- {tache}")
    else:
        print("Toutes les tâches de maintenance ont été exécutées.")

## Afficher l'adresse mémoire d'une variable
print(id(taches_maintenance))


if not taches_maintenance:
    print("Empty tasks")   

