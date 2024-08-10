### 생각한 알고리즘
 - while True문을 활용해서 주어진 조건대로 로직을 짜면 되는 간단한 문제였다.

### 오류
 - 오류는 발생하지 않았다.

### 알게된 것
 - for문으로 풀면
 -     for _ in range(1000):
         l = sorted(list(map(int, input().split())))
    
         if l[0] == l[1] == l[2] == 0:
            break
        
         if l[0] + l[1] <= l[2]:
            print("Invalid")
         else:
            if l[0] == l[1] == l[2]:
               print("Equilateral")
            elif l[0] == l[1] or l[1] == l[2] or l[0] == l[2]:
               print("Isosceles")
            else:
               print("Scalene")
   이렇게된다.
   입력의 마지막이 0 0처럼 정해져 있는 경우 for문과 while문을 이런식으로 활용해야 된다는 것을 알게되었다.
