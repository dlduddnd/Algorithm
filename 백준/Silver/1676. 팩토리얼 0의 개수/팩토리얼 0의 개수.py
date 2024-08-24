a = int(input())
sum = 1
count = 0

for tmp in range(1,a+1):
    sum = sum * tmp

for tmp in str(sum)[::-1]:
    if count == 0:
        if tmp == '0':
            count += 1
    else:
        if tmp == '0':
            count += 1
        else:
            break



print(count)
