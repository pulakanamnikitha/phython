q=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(q):
    print "yes"
else:
    print "no"
