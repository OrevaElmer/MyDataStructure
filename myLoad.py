import random

numbers = "2 4 7 8 9 0 3 1"
numberSplit = numbers.split(" ")
random.shuffle(numberSplit)
print(numberSplit)