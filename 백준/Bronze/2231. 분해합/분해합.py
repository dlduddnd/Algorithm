import sys
a = int(sys.stdin.readline())
l = []

for tmp in range(1,a):
    sum = tmp
    for tmp1 in str(tmp):
        sum = sum + int(tmp1)
    if sum == a:
        l.append(tmp)
        

if len(l) == 0:
    print(0)
else:
    print(min(l))