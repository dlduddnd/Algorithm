### 생각한 알고리즘
 - 이 문제는 리스트 전체를 뒤집는 것이 아닌 원하는 부분만 뒤집는 문제이기에 꽤나 생각이 어려웠다.그래서 chat GPT를 통해
   lst[start:end] = lst[start:end][::-1]를 이용하면 된다는 답을 얻었다.

### 오류 
 - 이 문제를 해결하기 위해 reverse(),reversed(),range,sort() 등 다양한 함수들을 생각해봤지만 문제가 해결되진않았다.
   그래서 길이가 짝수이면 l[i]와 l[j]를 뒤집고 l[i-1]와 l[j-1]을 뒤집으면 될 줄 알았다. 하지만 이 역시 i와 j의 수가 커지면 통하지 않는 방법이였다.

### 알게된 것
 -  lst[start:end] = lst[start:end][::-1] 이렇게 사용하면 부분만 뒤집힌 다는 것을 알고 Python의 위력에 상당히 충격을 받았다.
 -      basket = [i for i in range(1,n+1)]
        for x in range(m):
          i,j = map(int, input().split())
          temp = basket[i-1:j]
          temp.reverse()
          basket[i-1:j] = temp
    이렇게 리스트의 특정 부분만 따로 변수에 할당하는 것이 가능하다는 것을 알게되었다.
