a = int(input())

for tmp in range(0,a):
    print((a-(tmp+1)) * " " + (2*tmp+1) * "*")

for tmp2 in range(a,1,-1):
    print(((a+1)-tmp2) * " " + ((2*tmp2)-3) * "*")