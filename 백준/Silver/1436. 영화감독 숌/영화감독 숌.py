##count올리다가 입력값과 같아지면 나오기

import sys

a = int(sys.stdin.readline())
count = 0
z = 665

while True:
    
    if count == a:
        print(z)
        break
    
    z += 1

    if '666' in str(z):
        count += 1
    