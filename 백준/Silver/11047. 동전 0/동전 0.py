import sys
a,b = map(int,sys.stdin.readline().split())
l = []
for tmp in range(a):
    l.append(int(sys.stdin.readline()))

l.sort(reverse=True)
count = 0

while True:
    if b == 0:
        break
    for tmp in l:
        if b >= tmp:
            count += b // tmp  # count = 6
            b = b - (tmp*(b//tmp))  # b = 0
            break

print(count)
    
