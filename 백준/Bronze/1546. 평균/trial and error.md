### 생각한 알고리즘
- 처음에는 for문을 통해 입력을 받을 때마다 리스트에 넣고 그 리스트의 최댓값을 구한 후 입력 받은 값을 최댓값으로 나누어 100을 곱하고 그 값을 또 다른 리스트에 넣도록 했다.
  그리고 for문을 나와서 그 리스트의 합의 평균을 구하려 했었다.




### 오류
-     for tmp in range(a):
         b = map(int,input().split())
         l.append(b)
   우선 처음에 이렇게 해서 값을 입력받으려 했지만 줄바꿈 없이 입력을 받아야 했기에 오류가 발생했다.하지만 이는 멍청한 실수였다.
-      b = list(map(int,input().split()))
   그냥 for문도 필요 없이 이렇게 했으면 되는거였는데 말이다.


### 알게된 것
- 평균을 구할 때 numpy,statistics 모듈을 사용하여 구할 수 있다는 것을 알게되었다.
-     import numpy

      arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

      # 평균 구하기
      average = numpy.mean(arr)


-     import statistics

      arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      arr2 = [100, 90, 80, 10, 20, 30, 60, 70, 50, 40]

      # 평균 구하기
      result1 = statistics.mean(arr1)
      result2 = statistics.mean(arr2)
