v=[]

for i in xrange(999,99,-1):
    for j in xrange(999,99,-1):
         mult= i * j
         mult=str(mult)
         if mult[::1]==mult[::-1]:
             v.append(mult)
         
v=[int(i) for i in v]
print max(v)


