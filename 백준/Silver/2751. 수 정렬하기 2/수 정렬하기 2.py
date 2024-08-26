import sys

a = int(sys.stdin.readline())
l = []

for tmp in range(a):
    l.append(int(sys.stdin.readline()))

for tmp in sorted(l):
    print(tmp)
