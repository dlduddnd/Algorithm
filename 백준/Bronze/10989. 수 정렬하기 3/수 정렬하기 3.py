import sys
a = int(sys.stdin.readline())

count = [0] * 100001

for tmp in range(a):
    count[int(sys.stdin.readline())] += 1

for tmp in range(len(count)):
    if count[tmp] != 0:
        for tmp1 in range(count[tmp]):
            print(tmp)