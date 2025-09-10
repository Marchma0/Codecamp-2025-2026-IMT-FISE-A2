def remove_task(filename, id):
    """
    int x str -> bool
    Supprime une tâche d'un fichier texte en fonction de son identifiant.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        for l in lines:
            if l.strip().split('---')[0] == str(id):
                lines.remove(l)
                with open(filename, 'w') as file:
                    file.writelines(lines)
                print ("Deleted")
                return True
        else:
            print ("Not found")