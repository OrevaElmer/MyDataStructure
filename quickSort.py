#This program sort a list using quick sort:

def quickSort(list):
    if len(list) <= 1:
        return list

    lessThanPivot = []
    greaterThanPivot = []
    pivot = list[0]

    for item in list[1:]:
        if item <= pivot:
            lessThanPivot.append(item)
        else:
            greaterThanPivot.append(item)
    #print("%15s %1s %-15s" % (lessThanPivot, pivot, greaterThanPivot))
    return quickSort(lessThanPivot) + [pivot] + quickSort(greaterThanPivot)

number = [4, 1, 8, 2, 9, 7]
print(number)
print(quickSort(number))