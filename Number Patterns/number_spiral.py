num1 = int(input("Enter the value : "))
for i in range(1, 2 * num1):
    for j in range(1, 2 * num1):
        a = i
        b = j
        if a > num1:
            a = 2 * num1 - i
        if b > num1:
            b = 2 * num1 - j
        x = min(a, b)
        print(num1 - x + 1, end=" ")
    print()
