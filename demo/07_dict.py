mon_dict = {
    "cle": "valeur",
    3 : "Valeur de 3",
    "cle list": [1,3,4],
    3 : "valeur de 3"
    #[1,2,4] : "valeur de la liste"
}

print(mon_dict)

print(mon_dict["cle"])
print(mon_dict[3])
print(mon_dict["cle list"])

mon_dict["new key"]= "new value"
mon_dict[3] = "update key 3"
print(mon_dict)

## Itération sur les clés
for cle in mon_dict.keys():
    print(f"la clé {cle} valeur :{mon_dict[cle]}")

# Itération sur les valeur
for val in mon_dict.values():
    print(val)

# Itération sur les items sous forme de tuple

for tuple in mon_dict.items():
    cle, val = tuple
    print(f"la clé {cle} valeur :{val}")

## <=>

for cle, val in mon_dict.items():
    print(f"la clé {cle} valeur :{val}")

# del mon_dict["3"]
# <=>
print(mon_dict.pop(3))



print(mon_dict)

