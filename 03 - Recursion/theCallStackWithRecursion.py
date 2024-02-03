def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)
    
    
print(fact(3))