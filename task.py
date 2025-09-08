import argparse
import sys


def add_task(filename, description):
    print(f"Tâche ajoutée : {description} (dans {filename})")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    if len(lines) > 1:   
        id = lines[-1].split()[0].strip()
        new_id = int(id)
    else:
        new_id = 0

    new_id = new_id + 1

    with open(filename, 'a') as f:
        f.write(f"{new_id}  {description}\n")

    print("Nouvel ID :", new_id)
    return new_id




def modify_task(filename, task_id, new_description):
    modified = False
    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";", 1)  
            if parts[0] == str(task_id):
                lines.append(f"{task_id};{new_description}\n")
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
       

def remove_task(filename, task_id):
    print(f"Tâche {task_id} supprimée (dans {filename})")
    # à compléter

def show_tasks(filename):
    """ 
        Montre la liste des taches a effectuer avec leurs id
        input  : File path (str)
        output : liste des taches 
    """

    print(f"Affichage des tâches contenues dans {filename}... \n \n")

    toShow = ""
    with open(filename, 'r') as file:
        toShow += f"+{"":-^5}+{"":-^10}+\n"
        for line in file:
            line_id,content  = line.split("    ", 1)
            toShow += f"|{line_id:^5} | {content:^len(content)} |"
            toShow += f"+{"":-^5}+{"":-^10}+\n"

    print(toShow)

    return toShow


def delete (id: int, filename) -> str:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for l in lines:
            if l.strip().split()[0] == str(id):
                lines.remove(l)
                with open(filename, 'w') as file:
                    file.writelines(lines)
                print ("Deleted")
                break
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

    # Commande modify
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche existante")
    parser_modify.add_argument("id", type=int, help="Identifiant de la tâche")
    parser_modify.add_argument("description", nargs="+", help="Nouvelle description")

    # Commande rm
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id", type=int, help="Identifiant de la tâche")

    # Commande show
    subparsers.add_parser("show", help="Afficher toutes les tâches")

    args = parser.parse_args()

    # Parser final
    if args.command == "add":
        description = " ".join(args.description)
        add_task(args.filename, description)

    elif args.command == "modify":
        description = " ".join(args.description)
        modify_task(args.filename, args.id, description)

    elif args.command == "rm":
        remove_task(args.filename, args.id)

    elif args.command == "show":
        show_tasks(args.filename)

if __name__ == "__main__":
    main()
