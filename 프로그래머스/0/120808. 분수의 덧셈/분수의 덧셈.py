import math

def lcm(n1,n2):
     return (n1 * n2) // math.gcd(n1,n2)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = lcm(denom1,denom2)

    numer1 =  numer1 * (a//denom1)
    numer2 =  numer2 * (a//denom2)
    m = numer1 + numer2
    
    k = math.gcd(m,a)
    if k != 1:
        m = m // k
        a = a // k
        
    answer = [m,a]
    return answer

# 약분이 되는 경우