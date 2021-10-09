#This program search a list of names from another list of names:

import sys
#from treeHouse.load import load_strings
from loadNumberString import load_strings

fullname = load_strings(sys.argv[1])

searchNames = ["Fiona Dickens","Wendy McDonald","Yvonne McLean","Karen Grant"]

def binarySearch(collection, target):
    first = 0
    last = len(collection) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if collection[mid] == target:
            return mid
        elif collection[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None
     
for name in searchNames:
    indexOfnames = binarySearch(fullname, name)
    print(indexOfnames)

#print(linearSearch(fullname,'Felicity Davies'))
#This is how I called the sorted text or unsorted text:
# c:/xampp/htdocs/pythonLesson/myAlgorithm/myBinaryLinear.py names/unsorted.txt

    
    
