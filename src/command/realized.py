
from tools.date import isDate


def realized(filename,ID,date) -> bool:
    """
    Input : 
    filename : str : le nom du fichier texte
    ID : int : l'identifiant de la tâche à marquer comme réalisée
    date : str : la date de réalisation au format JJ/MM/AAAA
    Output :
    bool : True si la tâche a été marquée comme réalisée, False sinon
    """

    if not isDate(date):
        print("Erreur : la date doit être au format JJ/MM/AAAA.")
        return False
    

    modified = False
    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("---", 4)  
            if parts[0] == str(ID):
                lines.append(f"{ID}---{parts[1]}---{parts[2]}---{parts[3]}---{date}\n")
                modified = True
            else:
                lines.append(line + "\n")

    if modified:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Tâche {ID} réalisée le {date} avec succès.")
        return True
    else:
        print(f"Erreur : tâche {ID} non trouvée.")
        return False