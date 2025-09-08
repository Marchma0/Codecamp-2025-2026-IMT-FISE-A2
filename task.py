import argparse
import sys


def add_task(filename, description):
    print(f"Tâche ajoutée : {description} (dans {filename})")
    # à compléter

def modify_task(filename, task_id, new_description):
    print(f"Tâche {task_id} modifiée : {new_description} (dans {filename})")
    # à compléter

def remove_task(filename, task_id):
    print(f"Tâche {task_id} supprimée (dans {filename})")
    # à compléter

def show_tasks(filename):
    print(f"Affichage des tâches contenues dans {filename}")
    # à compléter




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
