num1 = int(input())
for j in range(2, num1 + 1):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        print(j)
