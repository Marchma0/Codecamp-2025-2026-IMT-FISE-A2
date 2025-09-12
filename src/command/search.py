from tools.date import compareDate
from src.command.show import display


def search_before(line_list,date):
    """
    input : 
    line_list : la liste des lignes du fichier text (int)
    date : la date entrée par l'uttilisateur (int)
    output :
    la liste de toutes les taches qui ont une date d'echeance avant cette date
    """
    lines_avant = []
    for line in line_list : 
        line = line.strip()
        current_date = line.split("---",4)[4]
        if compareDate(date,current_date) == -1 : 
            lines_avant.append(line)
    return lines_avant

def search_after(line_list,date):
    lines_avant = []
    for line in line_list : 
        line = line.strip()
        current_date = line.split("---",4)[4]
        if compareDate(date,current_date) == 1 : 
            lines_avant.append(line)
    return lines_avant
            
        
def search_task(lines,keyword):
    results = []
    for line in lines:
        if keyword.lower() in line.split("---")[1].lower():
            results.append(line)
    if len(results) == 0:
            print("No results found.")
    return(results)

def search_project(lines, project_name):
    tasks = []
    for line in lines:
        parts = line.split('---')
        if len(parts) >= 3:
            description = parts[1].strip()
            project = parts[2].strip()

            if project_name in project:
                tasks.append(description)
    if tasks:
        print("Tâches trouvées :", tasks)
    else:
        print("Aucun projet trouvé :", project_name)

    return tasks

def search_realized():
    ...

def search_not_realized():
    ...

def search(filename,
           keyword=None,
           project=None,
           isRealized = None,
           isNotRealized=None,
           before=None,
           after=None):
    with open(filename,"r") as f:
        lines = f.readline()
        if keyword :
            lines = search_task(lines,keyword)
        if project :
            lines = search_project(lines,project)
        if isRealized :
            lines = search_realized(lines,isRealized)
        if isNotRealized : 
            lines = search_not_realized(lines,isNotRealized)
        if before : 
            lines = search_before(lines,before)
        if after : 
            lines = search_after(lines,after)
        display(lines)
        
        
