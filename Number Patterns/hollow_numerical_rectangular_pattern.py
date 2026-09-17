num1 = int(input("Enter the number : "))

for i in range(1, num1 + 1):

    # First part
    for j in range(i, num1 + 1):
        if i == 1 or i == num1 or j == i or j == num1:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    # Second part
    for j in range(1, i):
        if i == num1:
            print(j, end=" ")
        elif j == i - 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    print()