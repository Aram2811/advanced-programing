c = 0
b = 0
for i in range(100):
    num1 = int(input())
    if num1 == b:
        c = c
    else:
        c = c + 1
    if 83 > num1:
        print("too small")
    elif 83 < num1:
        print("too large")
    else:
        print("It is true")
        print("number of attempts : ", c)
        break
    b = num1
