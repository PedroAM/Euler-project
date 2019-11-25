def collatz(n):
    l=[0]
    for i in xrange(1,n+1):
        count = 1
        while i != 1:
            if i%2 == 0:
                i = i/2
                count += 1
            elif i%2 != 0:
                i=3*i+1
                count +=1
        l.append(count)
    print "number: %d --> seq. length: %d" % (l.index(max(l)),max(l))
