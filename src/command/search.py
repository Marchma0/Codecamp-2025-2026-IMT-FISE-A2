from tools.date import compareDate
from src.command.show import display


def avant_date(line_list,date):
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

def avant_date(line_list,date):
    lines_avant = []
    for line in line_list : 
        line = line.strip()
        current_date = line.split("---",4)[4]
        if compareDate(date,current_date) == 1 : 
            lines_avant.append(line)
    return lines_avant
            
        
def search_task():
    ...

def search_project():
    ...

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
            lines = search_realized(lines,isNotRealized)
        if before : 
            lines = search_realized(lines,before)
        if after : 
            lines = search_realized(lines,after)
        display(lines)
        
        
