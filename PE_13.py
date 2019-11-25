
l=[]
carry=0
partial=[]

f=open("D:\MyWork\Dropbox\Project Euler\PE_13.txt","r")

for line in f.readlines():
    l.append(line)
f.close()    

for i in xrange(0,100):
    l[i]=l[i].strip('\n')

l=zip(*l) #l[x] becomes l[0][x] + l[1][x] + ...

for i in xrange(0,50):
    l[i]=[int(x) for x in l[i]] #convert tuple to list and str to int
    
l.reverse()

partial.append(sum(l[0]))
carry=partial[0]/10

for i in xrange(1,50):
    partial.append(sum(l[i])+carry)
    carry=partial[i]/10    
    
partial.reverse()

partial=[str(i)[2] for i in partial]

partial[0]='55'+partial[0]

partial= "".join(partial)

print partial[0:10]

