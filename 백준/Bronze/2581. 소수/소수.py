l = []
count = 0
a = int(input())
b = int(input())

for tmp in range(a,b+1):
    count = 0
    for tmp1 in range(1,tmp+1):
        if tmp % tmp1 == 0:
            count = count + 1
            
    
    if count == 2:
            l.append(tmp)

if len(l) == 0:
     
     print(-1)
else:     
     print(sum(l))
     print(min(l))