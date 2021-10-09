#This program search for a number from a list using recursive binary search:

def myRecursiveBinary(list, target):
    if len(list) == 0:
        return False
    else:
        midPoint = (len(list)) // 2
        if list[midPoint] == target:
            return True
        else:
            if list[midPoint] < target:
                return myRecursiveBinary(list[midPoint+1:],target)
            else: 
                return myRecursiveBinary(list[0:midPoint],target)
    return False    

numbers = [1,2,3,4,7,8,9]
result = myRecursiveBinary(numbers, 12)
print(result)
result = myRecursiveBinary(numbers, 1)
print(result)
result = myRecursiveBinary(numbers, 2)
print(result)
result = myRecursiveBinary(numbers, 4)
print(result)
result = myRecursiveBinary(numbers, 10)
print(result)
result = myRecursiveBinary(numbers, 9)
print(result)