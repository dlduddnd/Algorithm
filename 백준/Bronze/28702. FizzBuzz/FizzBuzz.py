import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
c = sys.stdin.readline()

if 'z' not in a:
    if (int(a) + 3) % 3 == 0 and (int(a) + 3) % 5 == 0:
        print("FizzBuzz")
    elif (int(a) + 3) % 3 == 0 and (int(a) + 3) % 5 != 0:
        print("Fizz")
    elif (int(a) + 3) % 3 != 0 and (int(a) + 3) % 5 == 0:
        print("Buzz")
    else:
        print(int(a)+3)

elif 'z' not in b:
    if (int(b) + 2) % 3 == 0 and (int(b) + 2) % 5 == 0:
        print("FizzBuzz")
    elif (int(b) + 2) % 3 == 0 and (int(b) + 2) % 5 != 0:
        print("Fizz")
    elif (int(b) + 2) % 3 != 0 and (int(b) + 2) % 5 == 0:
        print("Buzz")
    else:
        print(int(b)+2)

elif 'z' not in c:
    if (int(c) + 1) % 3 == 0 and (int(c) + 1) % 5 == 0:
        print("FizzBuzz")
    elif (int(c) + 1) % 3 == 0 and (int(c) + 1) % 5 != 0:
        print("Fizz")
    elif (int(c) + 1) % 3 != 0 and (int(c) + 1) % 5 == 0:
        print("Buzz")
    else:
        print(int(c)+1)
