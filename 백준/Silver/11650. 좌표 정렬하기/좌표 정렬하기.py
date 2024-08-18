a = int(input())
l = []


for tmp in range(a):
    x,y = map(int,input().split())
    l.extend([[x,y]])

k = sorted(l)

for tmp1 in k:
    print(tmp1[0],tmp1[1],end=" ")
    print()