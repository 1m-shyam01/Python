num1 = int(input("Enter the value : "))

# Upper Pyramid
for i in range(1, num1 + 1):
    for j in range(1, num1 - i + 1): print(" ", end=" ")
    for k in range(1, i * 2): print(i, end=" ")
    print()

# Lower Pyramid
for i in range(num1 - 1, 0, -1):
    for j in range(1, num1 - i + 1): print(" ", end=" ")
    for k in range(1, i * 2): print(i, end=" ")
    print()