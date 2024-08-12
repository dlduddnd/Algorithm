a = int(input())
l = []

for tmp in range(a):
    b = int(input())
    l.append(b)

for tmp1 in l:
    print(int(tmp1 // 25),end=" ")
    tmp1 = tmp1 - (25 * int(tmp1 // 25)) 
    
    print(int(tmp1 // 10),end=" ") 
    tmp1 = tmp1 - (10 * int(tmp1 // 10)) 
  
    print(int(tmp1 // 5),end=" ")
    tmp1 = tmp1 - (5 * int(tmp1 // 5))
   
    print(int(tmp1 // 1),end=" ")

    print()
