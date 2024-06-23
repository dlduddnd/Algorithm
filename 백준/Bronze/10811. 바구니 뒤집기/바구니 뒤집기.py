n,m = map(int,input().split())
l = []

for tmp in range(1,n+1):
    l.append(tmp)

for tmp2 in range(m):
    i,j = map(int,input().split())
    l[i-1:j] = l[i-1:j][::-1]

for tmp3 in l:
    print(tmp3) 