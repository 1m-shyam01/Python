num1 = int(input("Enter the value : "))

m = num1 - 1
nsp = 1

for i in range(1, num1 * 2):
    print(i, end=" ")
print()

for i in range(1, m + 1):
    a = 1

    for j in range(m + 1 - i):
        print(a, end=" ")
        a += 1

    for k in range(nsp):
        print(" ", end=" ")
        a += 1

    for j in range(m + 1 - i):
        print(a, end=" ")
        a += 1

    print()
    nsp += 2