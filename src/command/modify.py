from datetime import date

def modify_task(filename, task_id, new_description = None,new_project=None,new_due_date=None):
    """
    str x int x str -> bool
    Modifie la description d'une tâche existante dans un fichier texte.
    """
    modified = False
    lines = []
    done = str(date.today()) 

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("---", 4)  
            if parts[0] == str(task_id):
                lines.append(f"{task_id}---{new_description if new_description else parts[1] }---{new_project if new_project else parts[2]}---{new_due_date if new_due_date else parts[3]}---{parts[4]}\n")
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
       