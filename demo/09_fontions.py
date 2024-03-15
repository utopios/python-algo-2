

# def dire_bonjour(firstname, lastname, age = 0):
#     print(f"Bonjour {firstname} {lastname} {age}")





# # dire_bonjour("ABADI","Ihab", 36)
# # dire_bonjour("Jean", "DUPOND")

# # def carre(nombre) -> int:
# #     return nombre**2


# # def multiple_2(nombre):
# #     nombre *=2
# #     print(nombre)


# # a = 10

# # print(f"Avant {a} ")
# # # multiple_2(a)


# # def multipe_2():
# #     # print(a)
# #     # a = 2
# #     # print(a)
# #     global a
# #     a *= 2
# #     print(a)

# # multipe_2()

# # print(f"Après {a} ")

# liste_nom = []

# # def ajouter_nom(liste:list, nom):
# #     liste.append(nom)

# # ajouter_nom(liste_nom, "abadi")
# # ajouter_nom(liste_nom, "dupond")

# def ajouter_nom(nom):
#     #liste_nom = []
#     liste_nom.append(nom)
#     print(liste_nom)

# ajouter_nom("abadi")
# ajouter_nom("dupond")

# print(liste_nom)


### *args

def addition(*elements):
    total = 0
    for a in elements:
        total += a
    print(total)

addition(1,4,6,400)

def avec_kwargs(**kwargs):
    print(kwargs)

avec_kwargs(element1="val1", element2="val2")

def avec_args_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)


avec_args_kwargs(3,"element", True, element="val",element2="val2")