import argparse
import sys

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
       


def show_tasks(filename):
    """ 
    str -> str
    Affiche la liste des taches avec leur id dans un tableau.
    """
    print(f"Affichage des tâches contenues dans {filename}")
    toShow = ""
    with open(filename, 'r') as file:
        toShow += f"+{'':-^17}+{'':-^52}+{'':-^32}+\n"
        for line in file:
            line = line.strip()
            line_id,content,project  = line.split("---", 2)
            if not project : 
                project = "no project"
            if len(content) <= 50 :
                toShow += f"|{line_id:^16} | {content:^50} | {project:^30} |\n"
            else : 
                nb_retour_ligne = len(content)//50
                mid_line = nb_retour_ligne//2

                for i in range(nb_retour_ligne):
                    if i == mid_line : 
                        toShow += f"|{line_id:^16} | {content[i*50:i*50+50]:^50} | {project:^30} |\n"
                    else : 
                        toShow += f"|{'':^16} | {content[i*50:i*50+50]:^50} | {'':^30} |\n"
                toShow += f"|{'':^16} | {content[nb_retour_ligne*50:]:^50} | {'':^30} |\n"
            toShow += f"+{'':-^17}+{'':-^52}+{'':-^32}+\n"
    print(toShow)
    return toShow


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
            








def main():
    """
    Configuration du parser d'arguments 
    """

    parser = argparse.ArgumentParser(
        description="Gestionnaire de tâches en ligne de commande"
    )

    parser.add_argument(
        "filename",
        help="Nom du fichier contenant les tâches"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Commande add
    parser_add = subparsers.add_parser("add", help="Ajouter une nouvelle tâche")
    parser_add.add_argument("description", nargs="+", help="Description de la tâche")
    parser_add.add_argument("--projet", default=None, help="Nom du projet")


    # Commande modify
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche existante")
    parser_modify.add_argument("id", type=int, help="Identifiant de la tâche")
    parser_modify.add_argument("description", nargs="+", help="Nouvelle description")
    parser_modify.add_argument("--project", help="Nouveau projet (optionnel)", default=None)

    # Commande rm
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id", type=int, help="Identifiant de la tâche")

    # Commande show
    subparsers.add_parser("show", help="Afficher toutes les tâches")

    args = parser.parse_args()

    # Parser final
    if args.command == "add":
        description = " ".join(args.description)
        if args.projet :
            projet = "".join(args.projet)
            add_task(args.filename, description, projet)
        else: 
            add_task(args.filename, description)

    elif args.command == "modify":
        description = " ".join(args.description)
        modify_task(args.filename, args.id, description,new_project=args.project)

    elif args.command == "rm":
        remove_task(args.filename, args.id)

    elif args.command == "show":
        show_tasks(args.filename)

if __name__ == "__main__":
    main()
