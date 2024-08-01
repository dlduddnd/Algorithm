l  = []
x,y,w,h = map(int,input().split())

l.append(x)
l.append(y)
l.append(h-y)
l.append(w-x)

print(min(l))
