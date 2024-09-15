## set자료구조사용해서 교집합으로 풀이

l = set()
k = set()

a,b = map(int,input().split())

for tmp in range(a):
    
    l.add(input())

for tmp1 in range(b):
    
    k.add(input())

p = l&k
p = list(p)

print(len(p))

for tmp2 in sorted(p):
    print(tmp2)