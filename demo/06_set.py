# ma_liste = [5, 5, 5, 5, 5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(ma_liste)

# # On peut transformer une liste en un set 
# # pour en retirer tous les doublons
# # et l'organiser
# mon_set = set(ma_liste)
# print(mon_set)

# # faire un set vide:
# mon_set = set()
# print(mon_set)
# les accolades {} vides servent à la définition d'un dictionnaire vide

# On peut créer un set remplit via cette syntaxe
element = 'a'


mon_set_3 = {5, 1, 3, 4, 6,6, 'a', 'b', 'a', 'd', True, False, element}
for e in mon_set_3:
    print(hash(e))
print(mon_set_3)

# Pour ajouter un élément à un set, on se sert de la méthode .add()
mon_set = set()

mon_set.add(3)
mon_set.add('a')
mon_set.add('a')
print(mon_set)
mon_set.add('3')
print(mon_set)
mon_set.add(3.0) # spécificité ici, il considère que 3 == 3. malgrès les types différents
print(mon_set)

# Pour fusionner deux sets ensemble, il existe la fonction  .update()
set1 = {1,2,3,5,7}
set2 = {1,5,7,6}
set1.update(set2) # on met à jour set1 avec les valeurs de set2
print(set1)
print(set2)

# Pour retirer un élément d'un set
set1 = {1,2,3,5,25}
set1.remove(25) # Cause une erreur si l'élément n'est pas présent
print(set1)
set1 = {1,2,3,5,25}
set1.discard(25)  # Ne cause pas d'erreur en cas d'absence de l'élément
set1.discard(230)
print(set1)



mon_set_a = {1, 2, 3, 4, 5, 6}
mon_set_b = {5, 6, 7, 8, 9, 10}


# Tester s'il y a présence ou absence d'éléments en commun entre les deux sets
print(mon_set_a.isdisjoint(mon_set_b)) #False
print({25, 50, 99}.isdisjoint(mon_set_b)) #True


# Pour tester si un set fait partie ou non d'un autre set
print({1, 2, 3}.issubset({1, 2, 3, 4, 5, 6})) #True

# Pour tester si un set comprend un autre set
print({1, 2, 3, 4, 5, 6}.issuperset({1, 2, 3})) #True


mon_set_a = {1, 2, 3, 4, 5, 6}
mon_set_b = {5, 6, 7, 8, 9, 10}
print(mon_set_a.union(mon_set_b))  # UNION
print(mon_set_a.intersection(mon_set_b))  # INTERSECTION
print(mon_set_a.difference(mon_set_b))  # DIFFERENCE
print(mon_set_b.difference(mon_set_a))
print(mon_set_a.symmetric_difference(mon_set_b))  # DIFFERENCE SYMETRIQUE