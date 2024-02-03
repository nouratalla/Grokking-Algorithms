def countDown(i):
    print(i)
    if i <= 0:  # first part Base case
        return
    else:       # second part recursive case
        countDown(i-1)
        


countDown(20)    
    