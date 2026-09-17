num1 = int(input("Enter the number : "))
x = num1
small = 9
while x > 0:
    digit = x % 10
    if digit < small:
        small = digit
    x = x // 10
print(small)