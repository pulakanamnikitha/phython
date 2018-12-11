def odddig():
	n=int(input())
	p=[]
	while(n!=0):
		p.append(n%10)
		n//=10
	for i in range(len(p)-1,-1,-1):
		if p[i]%2!=0:
			print(p[i]),
try:
	odddig()
except:
	print('invalid')
