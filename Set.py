
def countdown(n): 
    while n > 0: 
        yield n 
        n -= 1 
list(countdown(3))        