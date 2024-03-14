# Ce qui est immuable est : Bool, str, int, bytes, range, tuple, frozenset
# ma_var = 25
# print(f"L'ID mémoire de notre variable est : {id(ma_var)}, sa valeur est {ma_var}")

# ma_var = 33
# print(f"L'ID mémoire de notre variable est : {id(ma_var)}, sa valeur est {ma_var}")

# ma_var = 25
# print(f"L'ID mémoire de notre variable est : {id(ma_var)}, sa valeur est {ma_var}")

# ma_var_b = 25
# print(f"L'ID mémoire de notre variable est : {id(ma_var_b)}, sa valeur est {ma_var_b}")


# Ce qui est muable est : List, dict et set
ma_liste = [1, 2, 3]
print(f"L'ID mémoire de notre variable est : {id(ma_liste)}, sa valeur est {ma_liste}")

ma_liste.append(5)
print(f"L'ID mémoire de notre variable est : {id(ma_liste)}, sa valeur est {ma_liste}")


ma_2e_variable_liste = ma_liste #MEME LISTE POINTEE PAR LES 2 VARIABLES --> MEME IDENTIFIANT
print(f"L'ID mémoire de notre variable est : {id(ma_liste)}, sa valeur est {ma_liste}")
print(f"L'ID mémoire de notre variable est : {id(ma_2e_variable_liste)}, sa valeur est {ma_2e_variable_liste}")

# ma_2e_variable_liste.append(5) #les 2 variables sont impactées car elle pointent la même liste
# print(ma_liste)
# print(ma_2e_variable_liste)

# ma_3e_variable_liste = ma_liste.copy() #Crée une nouvelle liste dans la mémoire
# print(f"L'ID mémoire de notre variable est : {id(ma_liste)}, sa valeur est {ma_liste}")
# print(f"L'ID mémoire de notre variable est : {id(ma_3e_variable_liste)}, sa valeur est {ma_3e_variable_liste}")
# ma_liste.append("nouvelle valeur") # Seule ma_liste est impactée car la 3e est une copie
# print(ma_liste)
# print(ma_2e_variable_liste)
# print(ma_3e_variable_liste)


# le hashage (condensat)
# print(hash(10))
# print(hash("10"))

# a = 1000
# b = 1000
# print(id(a))
# print(id(b))