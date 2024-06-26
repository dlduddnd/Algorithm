a = input()
b = 'abcdefghijklmnopqrstuvwxyz'

for tmp in b:
    if tmp in a:
        print(a.index(tmp),end = " ")
    else:
        print(-1,end=" ")
    