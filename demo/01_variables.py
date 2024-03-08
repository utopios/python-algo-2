# Print
print("hello world")
print('hello world')
# Print chaine sur plusieurs lignes
print("""test
    test

test""")

# print multiple avec des espaces
print(1, "test", 1.9)

# Une variable
ma_variable = 8
print(ma_variable)

# Si je veux commenter j'utilise le #
# Si je veux commenter plusiquer lignes, j'utilise "ctrl + K + C"
# Si je veux décommenter plusiquer lignes, j'utilise "ctrl + K + U"
# Si je veux commenter et/ou décommenter plusiquer lignes, j'utilise "ctrl + :"

#les numériques
var = 23  # int
print(type(var))
var = 23. # float
print(type(var))
var = 23.0 # float
print(type(var))

# le type chaine
var = "23.0" # str
print(type(var))

# les booléens
mon_bool = True
print(mon_bool)
mon_bool = False
print(mon_bool)

print(4 < 5)
print(4 > 5)
print(5 >= 5)
print(5 <= 5)
print(5 == 5)
print(5 != 5)

# input vide avec un print avant
print("saisir un entier")
var = input()
print(var)
print(type(var))

# Le cast (passer d'un type de variable à l'autre)
var_int = int(var)
print(var_int)
print(type(var_int))
var_float = float(var)
print(var_float)
print(type(var_float))

# input sur la même ligne
variable = input("Saisir un chiffre : ")
print(variable)