from tools.date import compareDate
from src.command.show import display
from tools.search_in_files import *

def search(filename,
           keyword=None,
           project=None,
           isRealized = None,
           isNotRealized=None,
           before=None,
           after=None):
    with open(filename,"r") as f:
        lines = f.readline()
        lines = isRealized(lines,isRealized)
        if keyword :
            lines = search_task(lines,keyword)
        if project :
            lines = search_project(lines,project)
        if before : 
            lines = search_before(lines,before)
        if after : 
            lines = search_after(lines,after)
        display(lines)
        
        
