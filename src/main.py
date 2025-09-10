import argparse

from command.remove import remove_task
from command.add import add_task
from command.modify import modify_task
from command.show import show_tasks

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
