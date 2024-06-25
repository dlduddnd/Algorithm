### 생각한 알고리즘
- 정수형으로 입력받은 다음 str()함수를 이용하여 for문에서 돌려서 리스트에 저장하고 sum()함수를 사용해서 해결하려 했는데
  문자열은 리스트에 append()가 되지 않아 tmp를 int형으로 다시 바꿔준 뒤 문제를 해결하였다.

### 오류
- str타입은 리스트에 append()되지 않아 오류가 발생했었다

### 알게된 것
- str타입은 리스트에 append()가 되지 않는다.
-      num = input()
       numbers = list(map(int,input()))
       print(sum(numbers))
   이 방법을 쓰면 훨씬 쉽다.
