n,k = map(int,input().split())
l = []
try:

   for tmp in range(1,n+1):
     if n % tmp == 0:
        l.append(tmp)
    
   print(l[k-1])
    
except Exception:
   print('0')


