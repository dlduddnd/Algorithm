n,m = map(int,input().split())

l = []
p = []

for tmp in range(n):
    l.append(list(map(int,input().split())))

for tmp2 in range(n):
    p.append(list(map(int,input().split())))


for tmp3 in range(n):
    for tmp4 in range(m):
        print(l[tmp3][tmp4] + p[tmp3][tmp4],end =" ")
    print("")