### 생각한 알고리즘
 - 우선 출력이 대문자로 되어야하기에 upper()함수를 이용하였고 문자열을 순회하면서 딕셔너리를 사용하여 key값을 문자로 두고 value를 반복된 횟수로 두어서 문제를 해결하고자 하였고
   가장 많이 사용된 알파벳이 여러개일 때 그것들을 리스트로 묶어 len()을 사용하여 길이가 2 이상이면 ?를 출력하고자 하였다.

### 오류
 - 딕셔너리로 해결하고자 했는데 딕셔너리는 인덱스가 되지도 않고 시퀀스도 아니여서 상당히 애를 먹었다.그래서 구글링을 통해 함수를 만들어 해결할 수 있겠다는 힌트를 얻었다.
   구글링을 통해 딕셔너리 value가 같은 것이 여러개 있을 때 key값을 찾는 함수를 참고했다.
   -     def find_keys(dict, val):
            return list(key for key, value in dict.items() if value == val)
     이렇게 하여 val에 딕셔너리 value의 최댓값을 인자로 넣어주면 가장 많이 사용된 알파벳들을 하나의 리스트로 묶을 수 있다.

### 알게된 것
 - a.itens()를 하면 key,value 모두 얻을 수 있다.
 - 함수를 굳이 만들지 않고
 -     [k for k,v in di.items() if max(di.values()) == v]
   이렇게 하는 것이 더 나았을 것 같다.
 - 딕셔너리에서 최댓값을 구하려면 max(c, key=c.__getitem__)를 사용해야 한다.
 -     word = input().upper()
       word_list = list(set(word))
       lst = []

       for i in word_list:
         count = word.count(i)
         lst.append(count)

       if lst.count(max(lst))>= 2:
         print("?")
       else:
         print(word_list[lst.index(max(lst))])
   또다른 풀이이다. 이 방법이 더 효율적인것 같다.

   
   
