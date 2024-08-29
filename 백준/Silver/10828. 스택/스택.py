from collections import deque
import sys

d = deque()
a = int(sys.stdin.readline())

for tmp in range(a):
    b = sys.stdin.readline().rstrip()

    if "push" in b:
        tmp,value = b.split()

        d.appendleft(int(value))

    if b == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()


    if b == 'size':
        print(len(d))

    if b == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    
    if b == "top":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])