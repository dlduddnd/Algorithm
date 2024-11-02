def solution(t, p):
    answer = 0
    a = len(p)
    l = []
    i = 0
    for tmp in range(int(t)):
        l.append(t[i:i+a])
        if i+a == len(t):
            break
        i += 1
    for tmp2 in l:
        if int(tmp2) <= int(p):
            answer += 1
    return answer


## p길이에 따라 i에서 i+1 , i+2, i+n.... 인덱스 추출해서 문자열 뽑아내고 수 비교

## 인덱스가 마지막이되면 빠져나오게 i+a == len(t)..?