logs = [
    "ERROR: Echec de connexion",
    "INFO: Maintenance",
    "INFO: Maintenance 2",
    "WARNING: Utilisation élevée de CPU"
]


def filtrer_logs(niveau):
    # resultat = []
    # for log in logs:
    #     if log.startswith(niveau):
    #         resultat.append(log)  
    # print(resultat)
    # return resultat

    # return [log for log in logs if log.startswith(niveau)]
    return list(filter(lambda log: log.startswith(niveau), logs))

def compter_logs():
    niveaux = set(log.split(':')[0] for log in logs)
    
    # resultat = {}
    # for niveau in niveaux:
    #     resultat[niveau] = sum(log.startswith(niveau) for log in logs)

    # return resultat
    return {niveau: sum(log.startswith(niveau) for log in logs) for niveau in niveaux}

print(compter_logs())