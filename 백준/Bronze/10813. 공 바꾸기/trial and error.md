### 생각한 알고리즘
 - 10810 공 넣기 문제와 비슷한 알고리즘으로 생각했다 다만 인덱스를 서로 바꾸는 과정을 추가시켰다.새로운 리스트를 이용하여 그 리스트를 매개로 하여 인덱스를 서로 바꾸었다.

### 오류
 - 오류는 발생하지 않았다.

### 알게된 것
 -     temp = box[i-1]
       box[i-1]=box[j-1]
       box[j-1]=temp
   처럼 리스트를 따로 생성하지 않고 변수만 따로 선언해주는 것으로 문제를 해결하는 것이 더 효율적인 것 같다.
