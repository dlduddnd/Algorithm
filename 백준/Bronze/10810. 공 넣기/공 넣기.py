n,m = map(int,input().split())

a = []

for tmp in range(n):
    a.append(0)

for tmp2 in range(m):
    i,j,k = map(int,input().split())
    a[i-1:j] = [k] * (j-i+1)

for tmp3 in a:
    print(tmp3,end=" ")
