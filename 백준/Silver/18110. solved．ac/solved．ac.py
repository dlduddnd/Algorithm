import sys
from collections import deque

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)


    
a = int(sys.stdin.readline())
l = []

if a == 0:
    print(0)
else:
    for tmp in range(a):
        l.append(int(sys.stdin.readline()))

    l.sort()
    l = deque(l)

    for tmp in range(my_round(a*(15/100))):
        l.popleft()
        l.pop()

    if len(l) == 0:
        print(0)

    else:
       print(my_round(sum(l)/len(l)))