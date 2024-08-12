a = int(input())
sum0 = 0
count = 1
l = []

for tmp in range(a-2):
    sum0 = sum0 + count
    l.append(sum0)
    count += 1 


print(sum(l))
print(3)

