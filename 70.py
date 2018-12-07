n=raw_input()
"""if all(c in '01' for c in n):
    print "Yes"
else:
    print "No"
    """
if not(n.translate(None,'01')):
    print "Yes"
else:
    print "No"
