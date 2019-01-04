s,n=map(int,(raw_input()).split())
if(s>n):
    p=s
else:
    p=n
while(True):
    if((p%s==0) and (p%n==0)):
        l=p
        break
    p+=1
print(l) 
