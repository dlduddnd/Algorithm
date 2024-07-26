while True:
    l = []
    s = ""
    a = int(input())

    if a == -1:
        break

    for tmp in range(1,a):
        if a % tmp == 0:
            l.append(tmp)

    if sum(l) == a:
        for tmp2 in range(len(l)):
            s += " " + "+" + " " + str(l[tmp2])
        p = s.lstrip(" +")
        print(str(a) + " " + "=" + " " + str(p))

   
    else:
        print(str(a) + " " + "is NOT perfect.")