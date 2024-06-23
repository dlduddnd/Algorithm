l = []

for tmp in range(10):
    a = int(input())
    b = a % 42
    l.append(b)
    

k = list(set(l))

print(len(k))