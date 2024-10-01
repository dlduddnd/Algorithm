import sys
a,b = map(int,sys.stdin.readline().split())
d = {}
i = 1
l = []
for tmp in range(a):
    k = sys.stdin.readline().rstrip()
    d[k] = i
    i += 1
    l.append(k)
    

for tmp in range(b):
    p = sys.stdin.readline().rstrip()
    if p.isdigit() == True:
        p = int(p)
        print(l[p-1])        

        
    else:
        print(d[p])