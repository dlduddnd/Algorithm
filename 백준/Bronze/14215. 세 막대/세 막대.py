l = list(map(int,input().split()))
l.sort()

while l[0]+l[1] <= l[2]:
    l[2] = l[2] - 1
    
print(sum(l))

