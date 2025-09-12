from tools.date import compareDate
from command.show import display
from tools.search_in_files import *

def search(filename,
           keyword=None,
           project=None,
           is_realized = 0,
           before=None,
           after=None):
    with open(filename,"r") as f:
        lines = f.readlines()
        lines = search_realized(lines,is_realized)

        if keyword :
            lines = search_task(lines,keyword)
        if project :
            print(lines)
            lines = search_project(lines,project)
            print(lines)
        if before : 
            lines = search_before(lines,before)
        if after : 
            lines = search_after(lines,after)

        display(lines)
        
        
