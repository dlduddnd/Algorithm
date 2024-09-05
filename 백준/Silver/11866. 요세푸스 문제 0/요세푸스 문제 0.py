import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())

l = deque()
k = []
for tmp in range(1,a+1):
    l.append(tmp)

while True:
    if len(l) == 0:
        break
    for tmp in range(b-1):
        l.append(l.popleft())

    k.append(str(l.popleft()))

print('<',', '.join(k),'>',sep="")