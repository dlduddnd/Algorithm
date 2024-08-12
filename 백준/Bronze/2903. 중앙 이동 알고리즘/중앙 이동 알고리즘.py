a = int(input())
l = []

while True:
    if len(l) == 0:
       b = 3
    l.append(b**2)
    b = 2*b-1
    
    if len(l) == a:
        break

print(l[a-1])

