a,b,c,d,e,f = map(int,input().split())


if a == 0:
    y = c//b
    x = f-(e*y)
    print(x//d,y,sep=" ")

elif d == 0:
    y = f//e
    x = c-(b*y)
    print(x//a,y,sep=" ")
     
     
else:
     l = (a*d)//a
     k = (a*d)//d

     a = a*l
     b = b*l
     c = c*l
     d = d*k
     e = e*k
     f = f*k

     y = (c-f)//(b-e)
     x = c-(b*y)

     print(x//a,y,sep=" ")