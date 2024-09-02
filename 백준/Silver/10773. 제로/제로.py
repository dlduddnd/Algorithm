import sys
a = int(sys.stdin.readline())
l = []

for tmp in range(a):
    l.append(int(sys.stdin.readline()))

    if l[-1] == 0:
        l.pop()
        l.pop()

print(sum(l))