a,b = map(int,input().split())
l = []
k = []
for tmp in range(1,a+1):
    if a % tmp == 0 and b % tmp == 0:
        l.append(tmp)

print(max(l))
print(max(l) * (a//max(l)) * (b//max(l)))