import sys

a,b = map(int,sys.stdin.readline().split())
sum = a
sum1 = b
i = 1
j = 1

for tmp in range(b-1):
    sum = sum * (a-i)
    i = i + 1

for tmp in range(b-1):
    sum1 = sum1 * (b-j)
    j = j + 1


if b == 0:
    print(1)
else:
    print(sum//sum1)