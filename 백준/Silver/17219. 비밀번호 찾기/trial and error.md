### 알고리즘
 - 입력받은 문자열을 split()을 이용해 나눠서 변수 2개에 할당해주고 딕셔너리에 key,value로 저장한 후 매핑시켜주는 방식으로 해결한다.

### 오류
 - 비밀번호를 매핑시켜주는 for문을 구현할 때 이중for문을 사용하는 방법밖에 생각나지 않아 시간초과가 여러번 발생했다
   ```
   for tmp in range(b):
      y = sys.stdin.readline().rstrip()
      print(d[y])
   ```
   이렇게 간단히 풀 수 있었는데 말이다

### 알게된 것
 - 딕셔너리로 풀어야된다는 것을 알고 있었지만 머릿속에 있는 동작을 코드로 구현하는 방식에 아직 부족함을 느꼈다.
 - 입력을 공백을 기준으로 나누어 변수에 할당하고 싶으면
   ```
    x = sys.stdin.readline().rstrip()
    g,h = x.split()
   ```
   이렇게 해주면 된다

 - ```
   x = 'a b c'
   g,h,p = x.split()
   ```
   이렇게해서 3개도 받을 수 있다.
    
