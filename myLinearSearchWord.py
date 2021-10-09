#This program search a list of names from another list of names:

import sys
#from treeHouse.load import load_strings
from loadNumberString import load_strings

fullname = load_strings(sys.argv[1])

searchNames2 = ["Andrea Bailey","Angela Baker","Anna Ball","Anne Bell","Audrey Berry","Ava Black"]

def linearSearch(collection, target):
    i = 0
    while i < len(collection):
        if collection[i] == target:
            return i
        i +=1
    return None

for name in searchNames2:
    indexOfName = linearSearch(fullname,name)
    print(indexOfName)
#print(linearSearch(fullname,'Felicity Davies'))
#This is how I called the sorted text or unsorted text:
# c:/xampp/htdocs/pythonLesson/myAlgorithm/myBinaryLinear.py names/unsorted.txt

    
    
