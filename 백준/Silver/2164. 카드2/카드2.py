import sys
from collections import deque

a = int(sys.stdin.readline())
l = deque()

for tmp in range(1,a+1):
    l.append(tmp)

# deque[1,2,3,4]

while len(l) != 1:
    l.popleft()
    l.append(l[0])
    l.popleft()

print(l[0])