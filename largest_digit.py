num1 = int(input("Enter the number : "))
x = num1
lar = 0
while x > 0:
    digit = x % 10
    if digit > lar:
        lar = digit
    x = x // 10
print(lar)