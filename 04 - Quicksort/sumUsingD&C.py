def sum(list):
    if len(list) == 1:
        return list.pop(0)
    else:
        return list.pop(0) + sum(list)
        

print(sum([2,4,6]))
    




   