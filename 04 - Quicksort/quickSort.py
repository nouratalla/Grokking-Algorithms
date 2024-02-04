def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        elementsSmallerThanPivot = [element for element in list[1:] if element <= pivot]
        elementsGreaterThanPivot = [element for element in list[1:] if element > pivot]
        return quicksort(elementsSmallerThanPivot) + [pivot] + quicksort(elementsGreaterThanPivot)
    

print(quicksort([10, 5, 2, 3]))