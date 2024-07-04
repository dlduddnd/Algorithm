l = []

for tmp in range(5):
    l.append(list(input()))

i = 0
j = 0


for tmp2 in range(len(max(l,key=len))):
     for tmp3 in l:
        if tmp2 < len(tmp3):

          print(tmp3[i],end="")
     i += 1
