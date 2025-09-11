import argparse

from command.remove import remove_task
from command.add import add_task
from command.modify import modify_task
from command.show import show_tasks
from command.realized import realized


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
    parser_add.add_argument("--description","-d", nargs="+", help="Description de la tâche")
    parser_add.add_argument("--project","-p" ,default=None, help="Nom du projet")
    parser_add.add_argument("--done_on",nargs="+",help="date_realisation")
    

    # Commande modify
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche existante")
    parser_modify.add_argument("id", type=int, help="Identifiant de la tâche")
    parser_modify.add_argument("--description","-d", nargs="+", help="Nouvelle description (optionnel)", default=None)
    parser_modify.add_argument("--project","-p" ,help="Nouveau projet (optionnel)", default=None)
    parser_modify.add_argument("--due", help="Nouvelle échéance (DD/MM/YYYY)", default=None)

    # Commande rm
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id", type=int, help="Identifiant de la tâche")

    # Commande show
    parser_show = subparsers.add_parser("show", help="Afficher toutes les tâches")
    parser_show.add_argument("--sorted", action="store_true", help="Trier les tâches par projet(optionnel)")

    # Commande realized
    parser_realized = subparsers.add_parser("realized", help="Réaliser une tâche")
    parser_realized.add_argument("id", type=int, help="Identifiant de la tâche")
    parser_realized.add_argument("--date", nargs=1, help="Date de réalisation (DD/MM/YYYY)", required=True)

    args = parser.parse_args()

    # Parser final
    if args.command == "add":
        description = " ".join(args.description)
        if args.project :
            project = "".join(args.project)
            add_task(args.filename, description, project)
        else: 
            add_task(args.filename, description)
    elif args.command == "modify":

        description  = " ".join(args.description)
        modify_task (args.filename, args.id, description,new_project=args.project,new_due_date=args.due)
                    
    elif args.command == "rm":
        remove_task(args.filename, args.id)

    elif args.command == "show":
        print(args.sorted)
        show_tasks(args.filename, args.sorted)
    
    elif args.command == "realized":
        date = "".join(args.date)
        realized(args.filename,args.id,date)

if __name__ == "__main__":
    main()
