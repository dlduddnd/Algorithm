a = int(input())
l = []


for tmp in range(a):
    a,b = map(str,input().split())
    a = int(a)
    l.append((a,b))

l.sort(key=lambda x : x[0])

for tmp1 in l:
    print(tmp1[0],tmp1[1])