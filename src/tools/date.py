def isDate(date):
    """
    str -> bool
    Vérifie si les dates sont de vrais dates conformes
    """
    msg = "La date n'est pas conforme"
    if date == "TBD":
        return True
    if len(date)!=10 or date[2]!="/" or date[5]!="/":
        print(msg)
        return False
    try:
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:10])
    except ValueError:
        print(msg)
        return False

    if month>12 or month<0:
        print(msg)
        return False
    
    daypermonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year%4==0):
        daypermonth= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day > daypermonth[month-1] or day < 0:
        print(msg)
        return False
    
    return True

def compareDate(d1,d2):
    """
    str x str -> int
    Compare de manière chronologique les dates :
    0 = d1 == d2
    1 = d1 < d2
    2 = d1 > d2
    """
    j1, m1, a1 = map(int, d1.split("/"))
    j2, m2, a2 = map(int, d2.split("/"))

    if(a1==a2 and m1==m2 and a1==a2):
        return 0
    if(a1<a2):
        return 1
    if(m1<m2):
        return 1
    if(j1<j2):
        return 1
    return -1


def sort_date(filename):
    """
    str -> List[str]
    sort les dates dans un fichier texte
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines.sort(key=lambda line: line.split('---')[3],cmp=compareDate)  # Trier par la date d'échéance (4ème élément)
    return lines
    


""" #Tests
assert isDate("10/12/2024")
assert isDate("29/02/2024")

assert not isDate("29/02/2025")
assert not isDate("10/12/2024caca") 
assert not isDate("10/13/2024")

assert compareDate("01/01/2024","01/01/2024") == 0
assert compareDate("01/01/2023","01/01/2024") == 1
assert compareDate("01/01/2024","01/01/2023") == -1
"""




