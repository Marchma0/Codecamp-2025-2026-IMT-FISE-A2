
from tools.date import sort_date


def show_tasks(filename):
    """ 
    str -> str
    Affiche la liste des taches avec leur id dans un tableau.
    """
    print(f"Affichage des tâches contenues dans {filename}")
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return display(lines)



def display(lineList):
    
    toShow = ""
    toShow += f"+{'':-^17}+{'':-^52}+{'':-^32}+{'':-^17}+{'':-^17}+\n"
    toShow += f"|{'ID':^16} | {'Description':^50} | {'Projet':^30} | {'Echeance':^15} | {'Realisation':^15} |\n"
    toShow += f"+{'':-^17}+{'':-^52}+{'':-^32}+{'':-^17}+{'':-^17}+\n"
    for line in lineList:
        line = line.strip()
        print(line)
        line_id,content,project,echeance,realized  = line.split("---", 4)
        if not project : 
            project = "no project"
        if len(content) <= 50 :
            toShow += f"|{line_id:^16} | {content:^50} | {project:^30} | {echeance:^15} | {realized:^15} |\n"
        else : 
            nb_retour_ligne = len(content)//50
            mid_line = nb_retour_ligne//2

            for i in range(nb_retour_ligne):
                if i == mid_line : 
                    toShow += f"|{line_id:^16} | {content[i*50:i*50+50]:^50} | {project:^30} | {echeance:^15} | {realized:^15} |\n"
                else : 
                    toShow += f"|{'':^16} | {content[i*50:i*50+50]:^50} | {'':^30} | {'':^15} | {'':^15} |\n"
            toShow += f"|{'':^16} | {content[nb_retour_ligne*50:]:^50} | {'':^30} | {'':^15} | {'':^15} |\n"
        toShow += f"+{'':-^17}+{'':-^52}+{'':-^32}+{'':-^17}+{'':-^17}+\n"
    print(toShow)
    return toShow


