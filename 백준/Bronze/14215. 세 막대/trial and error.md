### 생각한 알고리즘
 - 삼각형이 되기 위한 조건이 두 변의 길이의 합이 나머지 한 변의 길이보다 커야한다는 것을 이용하여 리스트를 받아 오름차순으로 정렬 후
   while문을 통해 가장 큰 값을 조정하여 합을 구하였다.

### 오류
 - 오류는 발생하지 않았다.

### 알게된 것
 - while문 코드를 for문으로 생각해보려 했는데 잘 생각이 나지 않아 gpt에게 물어본 결과
 -      l = list(map(int, input().split())) 
        l.sort()

       # l[0] + l[1] > l[2] 일 때까지 반복
       for i in range(l[2] - (l[0] + l[1]) + 1):
          if l[0] + l[1] > l[2]:
          break
          l[2] -= 1

       print(sum(l))
    이렇게 하면 된다는 코드를 받았다
    하지만 이 경우 2 2 2 일 때는 range(-1)이 되는데 어떻게 오류가 안나지?라는 생각이 들어서 찾아봤는데
    range함수의 인자가 양수가 아닌 경우에는 반복이 이루어지지 않는다고 한다.

- 그리고 처음에 l = sorted(list(map(int,input().split()))) 이렇게 하면 정렬까지 시킬 수 있다는 사실을 알게되었다.
