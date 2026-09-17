num1 = int(input("Enter the number : "))

total = 0

for i in range(1, num1):
    if num1 % i == 0:
        total = total + i

if total == num1:
    print("Perfect Number")
else:
    print("Not a Perfect Number")