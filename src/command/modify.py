

def modify_task(filename, task_id, new_description,new_project=None):
    """
    str x int x str -> bool
    Modifie la description d'une tâche existante dans un fichier texte.
    """
    modified = False
    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("---", 2)  
            if parts[0] == str(task_id):
                if new_project is None:
                    lines.append(f"{task_id}---{new_description}---{parts[2]}\n")
                else :
                    lines.append(f"{task_id}---{new_description}---{new_project}\n")
                modified = True
            else:
                lines.append(line + "\n")

    if modified:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Tâche {task_id} modifiée avec succès.")
        return True
    else:
        print(f"Erreur : tâche {task_id} non trouvée.")
        return False
       