import math
n,m=map(int,raw_input().split())
p=n*m
if math.sqrt(p).is_integer():
    print "yes"
else:
    print "no"
