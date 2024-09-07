import sys
from itertools import combinations
a,b = map(int,sys.stdin.readline().split())
l = sorted(list(map(int,input().split())))

k = list(combinations(l,3))
sum1 = 0
for tmp in k:
    if sum(tmp) > b:
        continue
    
    if sum1 == 0:
        sum1 = sum(tmp)
    else:
        if sum(tmp) > sum1:
            sum1 = sum(tmp)

print(sum1)