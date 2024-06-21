a = []
for tmp in range(28):
    n = int(input())
    a.append(n)

b = [x for x in range(1,31)]

c = list(set(b) - set(a))

c.sort()

for tmp2 in c:
    print(tmp2)