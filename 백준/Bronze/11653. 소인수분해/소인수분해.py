a = int(input())

for tmp in range(2,a+1):
    if a % tmp == 0:
        while a % tmp == 0:
            print(tmp)
            a //= tmp