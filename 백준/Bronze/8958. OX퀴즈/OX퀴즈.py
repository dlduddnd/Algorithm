a = int(input())
l = []
for tmp in range(a):
    l.append(input())

count = 0
i = 1

for tmp in l:
    for tmp1 in tmp:
        if tmp1 == 'O':
            count += i
            i += 1
            
        else:
            i = 1
    print(count)
    i = 1
    count = 0
    