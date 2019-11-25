import time

def isPrime(n):
    
    if n==1:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n%2 ==0 or n%3==0 or n%5==0 or n%7==0:
        return False

    for i in xrange(3,int(n**0.5+1),2):
        if n % i ==0:
            return False
        i +=1

    return True

def genPrimeUntil(n):

    p=[2]
    i=3

    for i in xrange(3,n):
        if isPrime(i):
            p.append(i)
        i = i+2

    return p

def getFactors(n):

    max_factor = int(n**0.5+1)
    factors=[]
    primes=genPrimeUntil(max_factor)
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
    return factors
        
