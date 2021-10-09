#This program search for a number using linear search:

def myLinear(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return f"{target} is in position {i}"
    return "Target not in list"

numbers = [1,2,3,4,7,8,9]
result = myLinear(numbers,13)
print(result)    
result = myLinear(numbers,1)
print(result) 
result = myLinear(numbers,2)
print(result) 
result = myLinear(numbers,3)
print(result) 
result = myLinear(numbers,7)
print(result) 
result = myLinear(numbers,14)
print(result) 
result = myLinear(numbers,9)
print(result) 