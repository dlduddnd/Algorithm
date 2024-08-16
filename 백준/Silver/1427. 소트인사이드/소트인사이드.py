a = int(input())
l = []

for tmp in str(a):
    l.append(tmp)

k = sorted(l,reverse=True)

for tmp in k:
    print(tmp,end="")