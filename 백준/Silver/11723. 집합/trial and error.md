### 알고리즘
 - 문제에서 주어진 조건대로 연산을 구현시켜주는데 핵심은 연산의 수가 3,000,000까지 가능하므로 list로 풀면 시간초과가 나므로 set으로 풀어야한다.

### 오류
 - list로 풀려고해서 시간초과 오류가 발생했었다

### 알게된 것
 - set은 대부분의 상황에서  O(1)의 시간이 보장되어 list보다 효율적인 부분이 있다.
 - 문자열을 입력받았을 때 in 연산자를 사용하는 방법도 있지만
```
  arr = list(input().split())
  c = arr[0]
  if c == 'add':
    s.add(int(arr[1]))
```
이런식으로 리스트로 받아서 인덱스를 활용하는 방법도 있다
