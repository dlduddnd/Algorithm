def find_keys(dict, val):
    return list(key for key, value in dict.items() if value == val)

a = input()
b = a.upper()

c = {}

for tmp in b:
    if tmp not in c:
        c[tmp] = 0
    else:
        c[tmp] += 1

w = find_keys(c, max(c.values()))

if len(w) >= 2:
    print("?")
else:
    print(max(c, key=c.__getitem__))
