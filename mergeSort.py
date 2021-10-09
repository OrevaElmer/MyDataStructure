def mergeSort(list):
    if len(list) <= 1:
        return list
    
    leftHalf, rightHalf = split(list)
    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)
    return merge(left, right)

def split(list):
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left,right):
    l = []
    i = 0
    j = 0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
    while j < len(right):
        l.append(right[j])
    return l

n = [12,90, 9,11,7,14]
print(mergeSort(n))