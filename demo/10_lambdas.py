
operation_addition = lambda a,b: a+b

# def calcule(a,b, operation):
#     if operation == "addition":
#         return a+b
#     ####

def calcule(a,b, operation):
    return operation(a,b)

print(calcule(10,20, operation_addition))

print(calcule(10,20, lambda a,b: a-b))

def filtre(a, liste_result:list):
    if a > 10:
        liste_result.append(a)

liste_a = [3,10,20,40]
liste_result = []
## sans fonction filter
for element in liste_a:
    # if element > 10:
    #     liste_result.append(element)
    filtre(element, liste_result)

print(liste_result)

## avec filter(lambda, liste)
liste_result = list(filter(lambda toto: toto > 10,liste_a))


liste_initial = [4,10,20,40]

print(list(map(lambda e : e**2, liste_initial)))
