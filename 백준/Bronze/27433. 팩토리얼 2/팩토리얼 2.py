def fac(n):
    r = 1
    for tmp in range(1,n+1):
          r = r * tmp
          
    return r

a = int(input())

print(fac(a))