num1 = int(input("Enter the value : "))

m = num1 - 1
nsp = 1

# First row
for i in range(num1 * 2 - 1):
    print("*", end=" ")

print()

# Remaining rows
for i in range(1, m + 1):

    # Left stars
    for j in range(m + 1 - i):
        print("*", end=" ")

    # Middle spaces
    for k in range(nsp):
        print(" ", end=" ")

    # Right stars
    for j in range(m + 1 - i):
        print("*", end=" ")

    print()

    nsp += 2