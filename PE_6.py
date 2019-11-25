def sum_sq(n):

    total=0

    for i in range (1,n+1):
        total = total+i**2

    return total

def sq_sum(n):

    total = 0

    for i in range (1,n+1):
        total = total + i

    total = total**2

    return total

print sq_sum(100) - sum_sq(100)
    
    
