a = int(input())
l = []
k = []

for tmp in range(a):
    b = input()
    l.append(b[0])
    b = b[::-1]
    k.append(b[0])

for tmp2,tmp3 in zip(l,k):
    print(tmp2,tmp3,sep="")