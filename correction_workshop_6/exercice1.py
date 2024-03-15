serveurs = [("serveur1", 80), ("serveur3", 50), ("serveur2", 10)]

def trier_serveur(serveurs, **kwargs):
    #cle_tri = kwargs["cle_tri"] if kwargs["cle_tri"] else "nom"
    cle_tri = kwargs.get("cle_tri", "nom") # dans le cadre ou la cle_tri n'existe pas la valeur par defaut serait nom
    index_tri = 0 if cle_tri == 'nom' else 1
    return sorted(serveurs, key=lambda serveur : serveur[index_tri])


print(trier_serveur(serveurs, cle_tri="cpu"))
print(trier_serveur(serveurs, cle_tri="nom"))