import math
import sys

a,b = map(int,sys.stdin.readline().split())
l = [True for tmp in range(b+1)]
l[1] = False
for tmp in range(2,int(math.sqrt(b))+1):
    if l[tmp] == True:
        j = 2
        while tmp*j <= b:
            l[tmp*j] = False
            j += 1


for tmp in range(a,b+1):
    if l[tmp] == True:
        print(tmp)