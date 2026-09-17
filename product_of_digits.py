num1 = int(input("Enter the number : "))
x = num1
mul = 1
while x > 0:
    rem = x % 10
    mul = mul*rem
    x = x // 10
print(mul)