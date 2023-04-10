num1 = int(input())
for i in range(num1):
    print("*" * (num1 - i) + " " * (2 * i) + "*" * (num1 - i))
