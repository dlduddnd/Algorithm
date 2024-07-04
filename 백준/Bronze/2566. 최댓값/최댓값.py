l = []

for tmp in range(9):
    l.append(list(map(int,input().split())))
maxvalue = 0
row = 0
col = 0

for tmp2 in range(9):
    for tmp3 in range(9):
        if l[tmp2][tmp3] >= maxvalue:
            maxvalue = l[tmp2][tmp3]
            row = tmp2 + 1
            col = tmp3 + 1

print(maxvalue)
print(row,col)