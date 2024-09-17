import sys
a = int(sys.stdin.readline())
l = set()
for tmp in range(a):
    
    b = sys.stdin.readline()

    if 'add' in b:
        x,c = b.split()
        l.add(c)

    if 'remove' in b:
        x,c = b.split()
        if c in l:
            l.remove(c)
        else:
            continue
    
    if 'check' in b:
        x,c = b.split()
        if c in l:
            print("1")
        else:
            print("0")
        
    if 'toggle' in b:
        x,c = b.split()
        if c in l:
            l.remove(c)
        else:
            l.add(c)
    
    if 'all' in b:
        l = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
        

    if 'empty' in b:
        l = set()
