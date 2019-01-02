n=int(input())
s=raw_input()
p=[]
for i in range(n):
    if s[i].lower() not in "aeiou":
        p.append(s[i])
p=''.join(p)
print p[::-1]
