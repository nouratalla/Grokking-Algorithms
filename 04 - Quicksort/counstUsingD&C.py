def count(list):
    if list == []:
        return 0
    else:
        list.pop(0)
        return 1 + count(list)
    
    
print(count([1,2,3,4,5,6]))