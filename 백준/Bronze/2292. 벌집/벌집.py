from sys import stdin
a = int(stdin.readline())

i = 2

n = 1



while True:
    if a == 1:
        print(1)
        break
    
    if i <= a <= (i + 6 * n) -1:
        print(n+1)
        break
    else:
        i = i + 6 * n
        n += 1