def multiple(n):

    total=0

    for i in range(n):
        if i%3==0 or i%5==0:
            total= total + i

    return total

print multiple(1000)
