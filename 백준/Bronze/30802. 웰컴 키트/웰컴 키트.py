N = int(input())
l = list(map(int,input().split()))
T,P = map(int,input().split())

count = 0

for tmp in l:
    if tmp != 0:
        if tmp // T == 0:
            count += 1
        
        elif tmp == T:
            count += 1
        
        elif tmp >= T and tmp % T != 0:
            count += ((tmp//T)+1)
        
        elif tmp >= T and tmp % T == 0:
            count += (tmp//T)


print(count)
print(N//P,N%P)