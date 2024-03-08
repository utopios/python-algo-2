# Les structures conditionnelles
mon_age = int(input("Quel est l'âge ? "))

if mon_age >= 21:  # La condition évaluée à l'entrée du bloc
    pass
    print("Vous êtes majeur aux USA, vous pouvez entrer !")
elif mon_age >= 18:  # La condition évaluée si la condition précédente n'est pas bonne
    print("Vous êtes majeur en France, vous pouvez entrer !")
else:  # Le chemin par défaut si aucune condition n'est bonne
    print("Vous êtes mineur, retournez en arrière !")

print("Code à la suite")

jour = int(input("Numéro jour de la semaine : "))


match jour:
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    #....
    
    case _:
        print("Erreur numéro")