n,k=map(int,raw_input().split())
if n>k:
    s=k
else:
    s=n
for i in range(1,s+1):
    if(n%i==0)and(k%i==0):
        max=i
print max
