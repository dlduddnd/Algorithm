L = int(input())
string = input()

# A의 유니코드는 65이므로 64를 뺴주면 1이된다

i = 0
sum = 0
for tmp in string:
    sum = sum + ((ord(tmp)-96) * (31 ** i))
    i += 1 

print(sum%1234567891)