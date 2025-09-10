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
