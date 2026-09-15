num1=int(input("Enter the value : "))
for i in range(1,num1+1):
    for j in range(1,num1+1-i):
        print("*",end=" ")
    print()