a = int(input())
l = []
for tmp in range(a):
    b = input()
    if b not in l:
        l.append(b)

l.sort(key=lambda x : (len(x), x))


for tmp in l:
    print(tmp)
