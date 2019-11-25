def small_mult(n):
    for i in range(1,21):
        if n%i !=0:
            return False
    return True

def iterate():
    i=1
    res=False
    while res==False:
        res=small_mult(i)
        i=i+1

    print "Menor divisor: " + str(i-1)
