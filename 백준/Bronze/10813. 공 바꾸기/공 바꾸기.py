n,m = map(int,input().split())

a = []
b = []

for tmp in range(n):
    a.append(tmp+1)
    b.append(0)

for tmp2 in range(m):
    i,j = map(int,input().split())
    b[0] = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = b[0]

for tmp3 in a:
    print(tmp3,end=" ")