### 알고리즘
 - 딕셔너리를 이용한 문제이고 isdigit()함수를 활용하여 key에 해당하는 value와 value에 해당하는 key를 매핑시켜주는 방식이다.
 - value에 해당하는 key를 찾을 때는 리스트의 인덱스를 활용하여 찾는다

### 오류
 - value를 통해 key를 찾는과정에서 [k for k, v in aa.items() if v == 'CC'] 이런식으로 for문을 사용하면 이중for문이 되어 시간초과가 발생한다

### 알게된 것
 - sys.stdin.readline()을 사용했을 때 개행문자가 포함되므로 rstrip()을 사용해 없애줄 수 있다.
 - any(tmp in p for tmp in '123456789') 이렇게 해서 숫자인지 확인하는 방법도 있다 하지만 저 방법도 for문을 사용하는 것이고 비효율적이므로 문제를 해결하기에는 적절하지 않다.
