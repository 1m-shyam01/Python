num1 = int(input("Enter the value : "))
for i in range(1, num1 + 1):
    for j in range(1, num1 - i + 1):
        print(" ", end=" ")
    if i == 1:
        print("1")
    elif i == num1:
        for j in range(1, 2 * num1):
            print(num1, end=" ")
        print()
    else:
        print(i, end=" ")
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")
        print(i)
