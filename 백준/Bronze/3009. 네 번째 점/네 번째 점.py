l = []
k = []
u = []

for tmp in range(3):
    a,b = map(int,input().split())
    l.append(a)
    k.append(b)


if l[0] == l[1]:
    u.append(l[2])

elif l[0] == l[2]:
    u.append(l[1])

elif l[1] == l[2]:
    u.append(l[0])

else:
    u.append(l[0])

if k[0] == k[1]:
    u.append(k[2])

elif k[0] == k[2]:
    u.append(k[1])

elif k[1] == k[2]:
    u.append(k[0])

else:
    u.append(k[0])

for tmp1 in u:
    print(tmp1,end=" ")
