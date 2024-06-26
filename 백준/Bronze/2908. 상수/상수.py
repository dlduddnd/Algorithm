a,b = map(int,input().split())
c = str(a)
d = str(b)

e = c[::-1]
f = d[::-1]

l = []
l.append(e)
l.append(f)

m = max(l)

print(m)
    
