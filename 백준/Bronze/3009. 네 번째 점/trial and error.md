### 생각한 알고리즘
 - x값과 y값을 따로 리스트에 저장한 후에 인덱스 0번 1번 같을 때 0번 2번 같을 때 1번 2번 같을때를 조건문으로 비교하여 남은 한 점을 구하였다.

### 오류
 - count함수를 써서 사용했을 떄는 오류가 발생했어서 위의 방식으로 해결하였다.

### 알게된 것
 - if-else 문을 조금 더 간결하게 작성할 수 있도록 노력해야 될 것 같다.
 -     elif l[1] == l[2]:
          u.append(l[0])

       else:
          u.append(l[0])
   이 부분을 
   -      else:
            u.append(l[0])
      그냥 이렇게 통합해도 된다.
