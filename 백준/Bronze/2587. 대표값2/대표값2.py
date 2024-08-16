l = []
for tmp in range(5):
    l.append(int(input()))


k = sorted(l)
print(sum(l)//5,k[2],sep="\n")