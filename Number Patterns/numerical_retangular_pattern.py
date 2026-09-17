num1=int(input("Enter the number : "))
for i in range(1,num1+1):
    for j in range(i,num1+1): print(j,end=" ")
    for j in range(1,i): print(j,end=" ")
    print()