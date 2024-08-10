a = int(input())
l = []
k = []

for tmp in range(a):
    x,y = map(int,input().split())
    l.append(x)
    k.append(y)

print((max(l)-min(l)) * (max(k)-min(k)))
