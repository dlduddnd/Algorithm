a = int(input())
l = []


for tmp in range(a):
    x,y = map(int,input().split())
    l.extend([[y,x]])

k = sorted(l)

for tmp1 in k:
    print(tmp1[1],tmp1[0],end=" ")
    print()