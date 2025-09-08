def modify_task(id,filename, new_description):
    modified = False
    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";", 1)  
            if parts[0] == str(id):
                lines.append(f"{id};{new_description}\n")
                modified = True
            else:
                lines.append(line + "\n")

    if modified:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Tâche {id} modifiée avec succès.")
        return True
    else:
        print(f"Erreur : tâche {id} non trouvée.")
        return False
