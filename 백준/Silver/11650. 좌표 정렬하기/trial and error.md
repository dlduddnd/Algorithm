### 알고리즘
 - 간단해 보이면서도 생각을 하게만드는 문제였다
 - x,y를 묶어서 리스트에 저장한 후 x를 기준으로 sort 함수를 사용해 정렬해주었다.

### 오류
 - 리스트 안에 두 변수를 동시에 묶어서 추가하는 과정에서 결과값을 알 수 없는 오류들이 여러 번 발생했었다.
 - 검색을 통해 extend함수를 사용하면 된다는 사실을 알게되어 활용하여 문제를 해결했다

### 알게된 것
 - extend()함수는 리스트에 여러개를 추가할 때 사용하는 함수이다
 - extend를 쓰려면 l.extend([[x, y]]) 이렇게 해야하고
 - append를 쓰려면 l.append([x,y]) 이렇게 하면 된다는 걸 알게되었고 왜 오류가 났었던 건지 알다가도 모르겠다.
