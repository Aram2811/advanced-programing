b = 0
c = 1
num1 = int(input())
for i in range(num1):
    d = b + c
    b = c
    c = d
print(d)
