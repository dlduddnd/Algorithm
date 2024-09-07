### 앍고리즘
 - 삼중 for문을 사용할 수도 있겠지만 itertools 라이브러리의 조합을 사용하여 최댓값을 판정해가는 로직을 구성하였다.

### 오류
 - 오류는 발생하지 않았다.

### 알게된 것
 - 삼중 for문을 사용하면
 ```python
N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three =  lst[i] + lst[j] + lst[k]
            if three > M:
                continue
            else:
                nlst.append(three)
print(max(nlst))
```
이렇게 표현이 가능하다

 - itertools 라이브러리를 사용하여 순열과 조합을 만들 수 있다는 것을 알게되었다.
