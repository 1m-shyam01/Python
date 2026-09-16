num1 = int(input("Enter the value : "))

# Upper Pyramid
for i in range(0, num1):
    for k in range(0, num1 - i):
        print(" ", end=" ")

    for j in range(0, 2 * i + 1):
        print(chr(65 + j), end=" ")

    print()


# Lower Pyramid
for i in range(num1 - 2, -1, -1):
    for k in range(0, num1 - i):
        print(" ", end=" ")

    for j in range(0, 2 * i + 1):
        print(chr(65 + j), end=" ")

    print()