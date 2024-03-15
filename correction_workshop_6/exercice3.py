def filtrer_ressources(ressources, *critere_filtrage, **kwargs):
    seuil = kwargs.get('seuil_utilisation')
    resultats = [res for res in ressources if all(res[crit[0]] == crit[1] for crit in critere_filtrage)]
    if seuil:
        resultats = [res for res in resultats if res['utilisation'] < seuil]
    return resultats

# Test
ressources = [
    {"type": "serveur", "capacité": "32GB", "utilisation": 60},
    {"type": "serveur", "capacité": "320GB", "utilisation": 60},
    {"type": "stockage", "capacité": "1TB", "utilisation": 80},
]
print(filtrer_ressources(ressources, ("type", "serveur"),("capacité", "32GB"), seuil_utilisation=70))
