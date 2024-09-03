### 앍고리즘
 - 큐를 사용해서 pop함수를 2번 사용하여 0과 그 앞 인덱스를 삭제시켜주었다

### 오류
 - 오류는 발생하지 않았다.

### 알게된 것
 - pop을 두번 사용하지 않고 값이 0이면 pop을 사용하고 그렇지 않으면 입력받은 수를 append하는 식의 로직도 구성해볼 수 있다
 ```python    
   if(num == 0): #num이 0이면 pop
        stk.pop()
    else:
        stk.append(num) #그게 아니라면 append = push
 ```  




