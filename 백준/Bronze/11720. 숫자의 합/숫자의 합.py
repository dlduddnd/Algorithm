a = int(input())
b = int(input())
l = []

for tmp in str(b):
    c = int(tmp)
    l.append(c)

print(sum(l))