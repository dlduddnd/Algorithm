import sys
a,b = map(int,sys.stdin.readline().split())

d = {}

for tmp in range(a):
    x = sys.stdin.readline().rstrip()
    g,h = x.split()
    d[g] = h

for tmp in range(b):
    y = sys.stdin.readline().rstrip()
    print(d[y])
    