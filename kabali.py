n=[]
l=[]
count=0
num=int(raw_input())
for i in xrange(0, num):
    n.append(raw_input())
for i in range(0,num):
    l.append(list(n[i]))
for i in range(0,num):
    l.append(l[i].sort())
m=l[0]
for i in range(num+1):
    if m==l[i]:
        count+=count+1
print count
