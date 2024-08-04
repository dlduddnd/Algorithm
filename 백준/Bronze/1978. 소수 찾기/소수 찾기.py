a = int(input())
while True:
    l= list(map(int,input().split()))
    if len(l) == a:
        break


count = 0
k = []

for tmp1 in l:
    count = 0
    if tmp1 > 1:
        for tmp2 in range(1,tmp1+1):
            if tmp1 % tmp2 == 0:
                count = count + 1

        if count == 2:
            k.append(tmp1)
            


print(len(k))
