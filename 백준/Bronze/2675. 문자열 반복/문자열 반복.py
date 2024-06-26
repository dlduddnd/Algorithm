a = int(input())
l = []
k = []

for tmp in range(a):
    r,s = input().split()
    r = int(r)
    for tmp2 in s:
      l.append(tmp2 * r)
    j = "".join(l)
    k.append(j)
    l.clear()

for tmp3 in k:
   print(tmp3)
