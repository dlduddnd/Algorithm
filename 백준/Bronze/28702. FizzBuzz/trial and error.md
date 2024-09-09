### 알고리즘
 - Fizz,Buzz,FizzBuzz이 입력에서 3번 연속 나올 수는 없다고 판단하여 'z'라는 공통된 문자가 입력값에 들어있는 지 조건을 나누어 문제를 해결하였다.

### 오류
 - 오류는 발생하지 않았다

### 알게된 것
 - 생각없이 푸려다보니 코드가 길어졌는데 간단히 하면
 - ```pythohn
   for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

   if n%3==0 and n%5==0:
     print('FizzBuzz')
   elif n%3==0:
     print('Fizz')
   elif n%5==0:
     print('Buzz')
   else:
     print(n)
  ```
