
def add_task(filename, description, project = "no project"):
    """ 
    str x str -> int
    Ajoute une nouvelle tâche à un fichier texte.
    Cette fonction prend en entrée le nom d'un fichier et la description d'une tâche, puis ajoute la tâche au fichier avec un identifiant unique généré à partir de la description. 
    Si le fichier n'existe pas, il est créé. La fonction affiche la tâche ajoutée et l'identifiant généré, puis retourne cet identifiant.
    """
    print(f"Tâche ajoutée : {description} (dans {filename}) pour projet {project}")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []


    new_id = int(id(description))

    with open(filename, 'a') as f:
        f.write(f"{new_id}---{description}---{project}\n")

    print("Nouvel ID :", new_id)
    return new_id