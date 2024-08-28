### 알고리즘
 - 시간초과 문제를 없애기 위해 import sys를 해주어 input을 sys.stdin.readline()으로 바꿔서 풀어주면된다

### 오류
 - 처음에 sys.stdin.readline()과 input()의 시간 차이가 어느정도 나는 지 모르고 input()으로만 해결하려고 생각했어서 계속 시간초과 오류가 발생했었다

### 알게된 것
 - input() 내장 함수는 sys.stdin.readline()과 비교해서 parameter로 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다는 것을 알게되었다.

