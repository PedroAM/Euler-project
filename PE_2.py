N=4000000
v=[0,1,2]
i=len(v)

# populate v with fib series up until N
while 1:
    v.insert(i,(v[i-1]+v[i-2]))
    if(v[i]>=N):
        del v[-1]
        break
    i=i+1

# set odd numbers to zero
for j in range(len(v)):
    if v[j] % 2 !=0:
        v[j]=0
    j=j+1

print v
print sum(v)
