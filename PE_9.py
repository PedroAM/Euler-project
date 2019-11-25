import sys

def triplet(s=1000):
    
    for a in xrange(2,1000):
        for b in xrange(a,1000):
           c=(a**2 + b**2)**0.5
           if a<b<c and a+b+c==s:
                print "a=%d, b=%d, c=%d" % (a,b,c)
                print "a*b*c=%d"% (a*b*c)
                sys.exit()
