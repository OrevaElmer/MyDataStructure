def myBinary(list, target):
    startPoint = 0
    endPoint = len(list) - 1
    while startPoint <= endPoint:
        midPoint = (startPoint + endPoint) // 2
        if list[midPoint] == target:
            return f"{target} is in position {midPoint}"
        else:
            if list[midPoint] < target:
                startPoint = midPoint + 1
            else:
                endPoint = midPoint - 1
    else:
        return "Target not in list"

numbers = [1,2,3,4,7,8,9]
result = myBinary(numbers, 12)
print(result)   
result = myBinary(numbers, 1)
print(result)            
result = myBinary(numbers, 2)
print(result)   
result = myBinary(numbers, 3)
print(result)   
result = myBinary(numbers, 4)
print(result)   
result = myBinary(numbers, 10)
print(result)   

