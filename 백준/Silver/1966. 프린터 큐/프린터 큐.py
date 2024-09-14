import sys
from collections import deque

a = int(sys.stdin.readline())
count = 0
k = []

for tmp in range(a):
    count = 0
    N,M = map(int,sys.stdin.readline().split())
    l = deque(map(int,sys.stdin.readline().split()))
    k = deque(i for i in range(len(l)))
    
    while M in k:
        while max(l) != l[0]:
            l.append(l.popleft())
            k.append(k.popleft())
        
        l.popleft()
        k.popleft()
        count+=1
    print(count)