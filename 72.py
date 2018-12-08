n=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(n):
    print "yes"
else:
    print "no"
