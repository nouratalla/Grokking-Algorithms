def max(list):
    if len(list) == 1 :
        return list[0]  # assume base cas is max number
    else:
       nextElement = list.pop(0)
       maxOfRestOfList = max(list)
       return nextElement if nextElement > maxOfRestOfList else maxOfRestOfList #comapre with base case
   
    
print(max([3,6,10,9,7]))
         
        
        