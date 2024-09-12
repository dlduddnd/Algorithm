import sys
a = int(sys.stdin.readline())
l = sorted(list(map(int,sys.stdin.readline().split())))

b = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))



for tmp in k:

    start = 0
    end = a-1

    while start <= end:
        mid = (start + end)//2

        if l[mid] == tmp:
            print("1")
            break

        elif l[mid] > tmp:
            end = mid - 1
            

        else:
            start = mid + 1

    if l[mid] != tmp:
        print(0)