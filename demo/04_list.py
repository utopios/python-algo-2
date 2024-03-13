# ma_liste = [
#     1,
#     2,
#     3,
#     4,
#     'bonjour',
#     True,
#     ['a', 'b', 33]
# ]


# print(ma_liste)

# print(ma_liste[0])
# print(ma_liste[6])

# # si on veut afficher un élément de la liste contenue dans la première
# print(ma_liste[6][2])

# # Modifier un élément à un index précis
# #ma_liste[10] = "test" # --> la liste n'est pas assez grande donc erreur
# ma_liste[0] = 80
# print(ma_liste)


ma_liste = [1, 4, 5, 2, 3, ]
print(ma_liste)
# pour trier une liste on utilise la methode .sort()
# ma_liste.sort()
# print(ma_liste)
# ma_liste.sort(reverse=True)
# print(ma_liste)

# pour trier une liste on peut aussi utiliser la fonction sorted()
# donne une nouvelle liste triée mais ne change pas ma_liste
print(sorted(ma_liste))
print(ma_liste)

# pour ajouter à la liste, on peut utiliser la méthode .append()
ma_liste.append(30)
ma_liste.append(30)
print(ma_liste)

# pour ajouter à un index précis, on utilise la méthode .insert(index, élément)
ma_liste.insert(2, 6)
print(ma_liste)

#pour ajouter une liste à la suite d'une autre 
ma_liste.extend(["Test", True])
print(ma_liste)
print(len(ma_liste))

# /!\ si on utilise append, on ajoutera la 2e liste DANS la première (en temps qu'élément)
ma_liste.append(["Test", True])
print(ma_liste)
print(len(ma_liste))

# pour retirer un élément avec son index et renvoyer l'élément
print(ma_liste.pop(9))
print(ma_liste)

# pour retirer un élément avec son contenu (la première qui correspond)
ma_liste.remove(30)
print(ma_liste)

# pour itérer sur une liste
for element in ma_liste:
    print(element)


# Avec un while
index = 0
while index < len(ma_liste)-1:
    print(f" element : {ma_liste[index]}, à la position : {index}")
    index+= 1