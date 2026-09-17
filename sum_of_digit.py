num1 = int(input("Enter the number : "))
x = num1
sum = 0
while x > 0:
    rem = x % 10
    sum = sum + rem
    x = x // 10
print(sum)