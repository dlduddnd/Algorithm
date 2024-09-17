import sys
a = int(sys.stdin.readline())

l = sorted(list(map(int,sys.stdin.readline().split())))

sum1 = 0
for tmp in range(a):
    sum1 += sum(l[0:tmp+1])

print(sum1)