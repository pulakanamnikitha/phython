ss=raw_input()
b=len(ss)
a=list(ss)
if b%2==0:
    m=b/2 - 1
    a[m]='*'
    a[m+1]='*'
else:
    m=b/2 - 1
    a[m+1]='*'
print "".join(a)
