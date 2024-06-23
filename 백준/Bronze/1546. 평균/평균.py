import statistics

a = int(input())

b = list(map(int,input().split()))

c = max(b)
l = []
for tmp in b:
    tmp = tmp/c * 100
    l.append(tmp)

result = statistics.mean(l)

print(round(result,2))