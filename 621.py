q=raw_input()
"""if all(c in '01' for c in q):
    print "Yes"
else:
    print "No"
    """
if not(q.translate(None,'01')):
    print "Yes"
else:
    print "No"
