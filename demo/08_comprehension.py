liste_a = [x for x in range(1,20)]
print(liste_a)
liste_b = [('EVEN' if x%2 == 0 else 'ODD') for x in liste_a]
print(liste_b)