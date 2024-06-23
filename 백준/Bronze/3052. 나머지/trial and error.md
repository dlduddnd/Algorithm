### 생각한 알고리즘
 - 처음에는 입력 받은 값의 나머지를 가지고 리스트를 for문으로 돌리면서 if문을 활용해 중복을 제거해보려 시도했다.
 -     l = []

       for tmp in range(10):
          a = int(input())
          b = a % 42
          for tmp2 in l:
             if b != tmp2:
                l.append(b)
            
       print(len(l))

### 오류
   -  리스트를 처음 초기화할 때 값이 아무것도 없어서 for문을 돌려도 아무것도 나오지 않아 0이 출력되었다.
      그래서 구글링을 통해 set를 이용하여 중복을 제거한 후 다시 리스트로 바꿔 len()을 사용하면 된다는 것을 알게되었다.

### 알게된 것
   - set을 사용하는 방법 말고 다른 방법을 찾아봤다
     for문을 사용하는 방법인데 리스트를 하나 더 생성하여 if A not in B를 활용하는 것이다.
   -     arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
         result = [] # 중복 제거된 값들이 들어갈 리스트

         for value in arr:
            if value not in result:
              result.append(value)

         print(result)

     
